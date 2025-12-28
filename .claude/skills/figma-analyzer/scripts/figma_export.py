#!/usr/bin/env python3
"""
Export design assets and metadata from Figma using the REST API.

Supports:
- Exporting frames/components as images (PNG, JPG, SVG, PDF)
- Extracting file and node metadata
- Extracting design tokens (colors, typography, effects)
- Batch export of multiple nodes
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from urllib.parse import urlparse, parse_qs

try:
    import requests
except ImportError:
    print("Error: requests package not installed")
    print("Install with: pip install requests")
    sys.exit(1)

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


FIGMA_API_BASE = "https://api.figma.com/v1"


def find_access_token() -> Optional[str]:
    """Find Figma access token using priority order.

    Priority order (highest to lowest):
    1. process.env (runtime environment variables)
    2. .claude/skills/figma-analyzer/.env (skill-specific config)
    3. .claude/skills/.env (shared skills config)
    4. .claude/.env (Claude global config)
    5. Project root .env
    """
    # Priority 1: Already in process.env
    token = os.getenv('FIGMA_ACCESS_TOKEN')
    if token:
        return token

    if load_dotenv:
        script_dir = Path(__file__).parent
        skill_dir = script_dir.parent  # .claude/skills/figma-analyzer
        skills_dir = skill_dir.parent   # .claude/skills
        claude_dir = skills_dir.parent  # .claude
        project_root = claude_dir.parent

        # Priority 2-5: Check .env files
        env_locations = [
            skill_dir / '.env',
            skills_dir / '.env',
            claude_dir / '.env',
            project_root / '.env',
        ]

        for env_file in env_locations:
            if env_file.exists():
                load_dotenv(env_file)
                token = os.getenv('FIGMA_ACCESS_TOKEN')
                if token:
                    return token

    return None


def parse_figma_url(url: str) -> Tuple[str, Optional[str]]:
    """Parse Figma URL to extract file key and node ID.

    Supports formats:
    - https://www.figma.com/file/{key}/{name}
    - https://www.figma.com/file/{key}/{name}?node-id={id}
    - https://www.figma.com/design/{key}/{name}
    - https://www.figma.com/design/{key}/{name}?node-id={id}

    Returns:
        Tuple of (file_key, node_id or None)
    """
    parsed = urlparse(url)

    # Extract file key from path
    path_parts = parsed.path.strip('/').split('/')
    if len(path_parts) >= 2 and path_parts[0] in ('file', 'design'):
        file_key = path_parts[1]
    else:
        raise ValueError(f"Invalid Figma URL format: {url}")

    # Extract node ID from query params
    query_params = parse_qs(parsed.query)
    node_id = None
    if 'node-id' in query_params:
        # Node IDs in URLs use '-' but API uses ':'
        node_id = query_params['node-id'][0].replace('-', ':')

    return file_key, node_id


def make_request(
    endpoint: str,
    token: str,
    params: Optional[Dict] = None,
    max_retries: int = 3
) -> Dict[str, Any]:
    """Make authenticated request to Figma API with retry logic."""
    headers = {
        'X-Figma-Token': token,
        'Content-Type': 'application/json'
    }

    url = f"{FIGMA_API_BASE}{endpoint}"

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 429:
                # Rate limited - wait and retry
                wait_time = int(response.headers.get('Retry-After', 60))
                print(f"Rate limited. Waiting {wait_time}s...")
                time.sleep(wait_time)
                continue

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise
            wait_time = 2 ** attempt
            print(f"Retry {attempt + 1} after {wait_time}s: {e}")
            time.sleep(wait_time)

    return {}


def get_file_metadata(file_key: str, token: str) -> Dict[str, Any]:
    """Get file metadata and structure."""
    return make_request(f"/files/{file_key}", token)


def get_node_metadata(
    file_key: str,
    node_ids: List[str],
    token: str
) -> Dict[str, Any]:
    """Get metadata for specific nodes."""
    params = {'ids': ','.join(node_ids)}
    return make_request(f"/files/{file_key}/nodes", token, params)


def get_image_urls(
    file_key: str,
    node_ids: List[str],
    token: str,
    scale: int = 2,
    format: str = 'png'
) -> Dict[str, str]:
    """Get image export URLs for nodes."""
    params = {
        'ids': ','.join(node_ids),
        'scale': scale,
        'format': format
    }
    response = make_request(f"/images/{file_key}", token, params)
    return response.get('images', {})


def download_image(url: str, output_path: Path, verbose: bool = False) -> bool:
    """Download image from URL to local path."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        if verbose:
            print(f"Downloaded: {output_path}")
        return True

    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False


def get_file_styles(file_key: str, token: str) -> Dict[str, Any]:
    """Get published styles from file."""
    return make_request(f"/files/{file_key}/styles", token)


def extract_design_tokens(file_data: Dict[str, Any]) -> Dict[str, Any]:
    """Extract design tokens from file metadata."""
    tokens = {
        'colors': {},
        'typography': {},
        'effects': {},
        'grids': {}
    }

    # Process styles from document
    if 'styles' in file_data:
        for style_id, style_data in file_data['styles'].items():
            style_type = style_data.get('styleType', '')
            style_name = style_data.get('name', style_id)

            if style_type == 'FILL':
                tokens['colors'][style_name] = {
                    'id': style_id,
                    'description': style_data.get('description', '')
                }
            elif style_type == 'TEXT':
                tokens['typography'][style_name] = {
                    'id': style_id,
                    'description': style_data.get('description', '')
                }
            elif style_type == 'EFFECT':
                tokens['effects'][style_name] = {
                    'id': style_id,
                    'description': style_data.get('description', '')
                }
            elif style_type == 'GRID':
                tokens['grids'][style_name] = {
                    'id': style_id,
                    'description': style_data.get('description', '')
                }

    return tokens


def find_all_nodes(node: Dict[str, Any], node_type: Optional[str] = None) -> List[Dict[str, Any]]:
    """Recursively find all nodes of a given type."""
    results = []

    if node_type is None or node.get('type') == node_type:
        results.append(node)

    for child in node.get('children', []):
        results.extend(find_all_nodes(child, node_type))

    return results


def export_frames(
    file_key: str,
    token: str,
    node_ids: Optional[List[str]] = None,
    output_dir: Path = Path('output'),
    scale: int = 2,
    format: str = 'png',
    verbose: bool = False
) -> List[Path]:
    """Export frames as images."""
    exported = []

    # If no node IDs specified, get top-level frames from first page
    if not node_ids:
        file_data = get_file_metadata(file_key, token)
        document = file_data.get('document', {})
        pages = document.get('children', [])

        if pages:
            first_page = pages[0]
            frames = find_all_nodes(first_page, 'FRAME')
            # Only get direct children (top-level frames)
            top_frames = [f for f in frames if f.get('parent', {}).get('type') == 'CANVAS']
            if not top_frames:
                # Fallback: use all frames from first page children
                top_frames = [c for c in first_page.get('children', []) if c.get('type') == 'FRAME']
            node_ids = [f['id'] for f in top_frames[:10]]  # Limit to 10 frames

    if not node_ids:
        print("No frames found to export")
        return exported

    if verbose:
        print(f"Exporting {len(node_ids)} nodes...")

    # Get image URLs
    image_urls = get_image_urls(file_key, node_ids, token, scale, format)

    # Download images
    for node_id, url in image_urls.items():
        if url:
            # Sanitize node ID for filename
            safe_id = node_id.replace(':', '-')
            output_path = output_dir / f"frame_{safe_id}.{format}"
            if download_image(url, output_path, verbose):
                exported.append(output_path)

    return exported


def main():
    parser = argparse.ArgumentParser(
        description='Export design assets from Figma',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Export a specific frame
  %(prog)s --url "https://www.figma.com/file/ABC/Design?node-id=1-234" \\
    --output design.png

  # Get file metadata only
  %(prog)s --url "https://www.figma.com/file/ABC/Design" \\
    --metadata-only --output metadata.json

  # Extract design tokens
  %(prog)s --url "https://www.figma.com/file/ABC/Design" \\
    --extract-tokens --output tokens.json

  # Export multiple frames
  %(prog)s --url "https://www.figma.com/file/ABC/Design" \\
    --node-ids "1-234,1-235" --output frames/
        """
    )

    parser.add_argument('--url', required=True, help='Figma file or frame URL')
    parser.add_argument('--output', default='output', help='Output path')
    parser.add_argument('--scale', type=int, default=2, choices=[1, 2, 3, 4],
                        help='Export scale (default: 2)')
    parser.add_argument('--format', default='png', choices=['png', 'jpg', 'svg', 'pdf'],
                        help='Export format (default: png)')
    parser.add_argument('--node-ids', help='Comma-separated node IDs to export')
    parser.add_argument('--metadata-only', action='store_true',
                        help='Only fetch metadata, no image export')
    parser.add_argument('--extract-tokens', action='store_true',
                        help='Extract design tokens')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Verbose output')

    args = parser.parse_args()

    # Get access token
    token = find_access_token()
    if not token:
        print("Error: FIGMA_ACCESS_TOKEN not found")
        print("Set via: export FIGMA_ACCESS_TOKEN='your-token'")
        print("Or create .env file with: FIGMA_ACCESS_TOKEN=your-token")
        sys.exit(1)

    # Parse URL
    try:
        file_key, url_node_id = parse_figma_url(args.url)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    if args.verbose:
        print(f"File key: {file_key}")
        if url_node_id:
            print(f"Node ID: {url_node_id}")

    output_path = Path(args.output)

    # Metadata only mode
    if args.metadata_only:
        if args.verbose:
            print("Fetching metadata...")

        file_data = get_file_metadata(file_key, token)

        # If specific node requested, get that node's data
        if url_node_id:
            node_data = get_node_metadata(file_key, [url_node_id], token)
            file_data['requested_node'] = node_data

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(file_data, f, indent=2)

        print(f"Metadata saved to: {output_path}")
        return

    # Extract tokens mode
    if args.extract_tokens:
        if args.verbose:
            print("Extracting design tokens...")

        file_data = get_file_metadata(file_key, token)
        tokens = extract_design_tokens(file_data)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            json.dump(tokens, f, indent=2)

        print(f"Design tokens saved to: {output_path}")
        return

    # Export images
    node_ids = None
    if args.node_ids:
        # Convert from URL format (1-234) to API format (1:234)
        node_ids = [nid.replace('-', ':') for nid in args.node_ids.split(',')]
    elif url_node_id:
        node_ids = [url_node_id]

    # Determine if output is a directory or single file
    if output_path.suffix in ['.png', '.jpg', '.svg', '.pdf']:
        # Single file output
        output_dir = output_path.parent
        single_file = True
    else:
        # Directory output
        output_dir = output_path
        single_file = False

    exported = export_frames(
        file_key=file_key,
        token=token,
        node_ids=node_ids,
        output_dir=output_dir,
        scale=args.scale,
        format=args.format,
        verbose=args.verbose
    )

    # If single file output and we got one file, rename it
    if single_file and len(exported) == 1:
        exported[0].rename(output_path)
        print(f"Exported: {output_path}")
    else:
        print(f"Exported {len(exported)} files to: {output_dir}")


if __name__ == '__main__':
    main()
