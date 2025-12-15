#!/usr/bin/env python3
"""
Documentation Generator Script

This script analyzes code files and generates documentation reports.
It checks for:
- Missing JSDoc/docstrings on public APIs
- Outdated README sections
- Missing changelog entries
- Invalid links in documentation
"""

import os
import re
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple

# ============================================================================
# Configuration
# ============================================================================

CONFIG = {
    "source_extensions": [".ts", ".tsx", ".js", ".jsx", ".py", ".go"],
    "doc_extensions": [".md", ".rst"],
    "ignore_dirs": ["node_modules", ".git", "dist", "build", "__pycache__", "venv"],
    "min_doc_coverage": 80,  # Percentage
}

# ============================================================================
# Code Analysis
# ============================================================================

def find_source_files(root_dir: str) -> List[Path]:
    """Find all source code files in the project."""
    source_files = []

    for root, dirs, files in os.walk(root_dir):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if d not in CONFIG["ignore_dirs"]]

        for file in files:
            if any(file.endswith(ext) for ext in CONFIG["source_extensions"]):
                source_files.append(Path(root) / file)

    return source_files


def analyze_typescript_file(file_path: Path) -> Dict:
    """Analyze a TypeScript/JavaScript file for documentation coverage."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    results = {
        "file": str(file_path),
        "exports": [],
        "documented": [],
        "undocumented": [],
    }

    # Find exported functions/classes
    export_patterns = [
        r"export\s+(async\s+)?function\s+(\w+)",
        r"export\s+class\s+(\w+)",
        r"export\s+const\s+(\w+)",
        r"export\s+default\s+(function\s+)?(\w+)",
    ]

    # Find JSDoc comments
    jsdoc_pattern = r"/\*\*[\s\S]*?\*/\s*(?:export\s+)?(async\s+)?(function|class|const)\s+(\w+)"

    documented = set()
    for match in re.finditer(jsdoc_pattern, content):
        name = match.group(3)
        documented.add(name)
        results["documented"].append(name)

    # Find all exports
    all_exports = set()
    for pattern in export_patterns:
        for match in re.finditer(pattern, content):
            name = match.groups()[-1]
            if name and name not in ["default", "async"]:
                all_exports.add(name)

    results["exports"] = list(all_exports)
    results["undocumented"] = list(all_exports - documented)

    return results


def analyze_python_file(file_path: Path) -> Dict:
    """Analyze a Python file for documentation coverage."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    results = {
        "file": str(file_path),
        "exports": [],
        "documented": [],
        "undocumented": [],
    }

    # Find function and class definitions
    def_pattern = r"^(def|class)\s+(\w+)"
    docstring_pattern = r'^(def|class)\s+(\w+)[^:]*:\s*\n\s*"""'

    documented = set()
    for match in re.finditer(docstring_pattern, content, re.MULTILINE):
        documented.add(match.group(2))
        results["documented"].append(match.group(2))

    all_defs = set()
    for match in re.finditer(def_pattern, content, re.MULTILINE):
        name = match.group(2)
        if not name.startswith("_"):  # Skip private
            all_defs.add(name)

    results["exports"] = list(all_defs)
    results["undocumented"] = list(all_defs - documented)

    return results


def analyze_file(file_path: Path) -> Optional[Dict]:
    """Analyze a source file based on its extension."""
    ext = file_path.suffix

    if ext in [".ts", ".tsx", ".js", ".jsx"]:
        return analyze_typescript_file(file_path)
    elif ext == ".py":
        return analyze_python_file(file_path)

    return None


# ============================================================================
# Documentation Analysis
# ============================================================================

def find_doc_files(root_dir: str) -> List[Path]:
    """Find all documentation files in the project."""
    doc_files = []

    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in CONFIG["ignore_dirs"]]

        for file in files:
            if any(file.endswith(ext) for ext in CONFIG["doc_extensions"]):
                doc_files.append(Path(root) / file)

    return doc_files


def check_links(file_path: Path) -> List[Dict]:
    """Check for broken links in a markdown file."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    issues = []

    # Find markdown links [text](url)
    link_pattern = r"\[([^\]]+)\]\(([^)]+)\)"

    for match in re.finditer(link_pattern, content):
        text, url = match.groups()

        # Check relative links
        if not url.startswith(("http://", "https://", "#", "mailto:")):
            linked_path = file_path.parent / url
            if not linked_path.exists():
                issues.append({
                    "type": "broken_link",
                    "text": text,
                    "url": url,
                    "line": content[:match.start()].count("\n") + 1,
                })

    return issues


def check_readme_sections(readme_path: Path) -> List[Dict]:
    """Check README for required sections."""
    required_sections = [
        "Installation",
        "Usage",
        "Contributing",
        "License",
    ]

    recommended_sections = [
        "Features",
        "Configuration",
        "API",
        "Examples",
    ]

    issues = []

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read().lower()

    for section in required_sections:
        if f"## {section.lower()}" not in content and f"# {section.lower()}" not in content:
            issues.append({
                "type": "missing_section",
                "section": section,
                "severity": "error",
            })

    for section in recommended_sections:
        if f"## {section.lower()}" not in content and f"# {section.lower()}" not in content:
            issues.append({
                "type": "missing_section",
                "section": section,
                "severity": "warning",
            })

    return issues


# ============================================================================
# Report Generation
# ============================================================================

def generate_report(root_dir: str) -> Dict:
    """Generate a comprehensive documentation report."""
    report = {
        "generated_at": datetime.now().isoformat(),
        "root_dir": root_dir,
        "code_analysis": {
            "total_files": 0,
            "total_exports": 0,
            "documented": 0,
            "undocumented": 0,
            "coverage_percentage": 0,
            "files": [],
        },
        "doc_analysis": {
            "total_files": 0,
            "link_issues": [],
            "readme_issues": [],
        },
        "recommendations": [],
    }

    # Analyze source files
    source_files = find_source_files(root_dir)
    report["code_analysis"]["total_files"] = len(source_files)

    total_exports = 0
    total_documented = 0

    for file_path in source_files:
        try:
            analysis = analyze_file(file_path)
            if analysis:
                report["code_analysis"]["files"].append(analysis)
                total_exports += len(analysis["exports"])
                total_documented += len(analysis["documented"])
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")

    report["code_analysis"]["total_exports"] = total_exports
    report["code_analysis"]["documented"] = total_documented
    report["code_analysis"]["undocumented"] = total_exports - total_documented

    if total_exports > 0:
        report["code_analysis"]["coverage_percentage"] = round(
            (total_documented / total_exports) * 100, 2
        )

    # Analyze documentation files
    doc_files = find_doc_files(root_dir)
    report["doc_analysis"]["total_files"] = len(doc_files)

    for doc_path in doc_files:
        try:
            link_issues = check_links(doc_path)
            if link_issues:
                report["doc_analysis"]["link_issues"].extend([
                    {"file": str(doc_path), **issue} for issue in link_issues
                ])

            if doc_path.name.lower() == "readme.md":
                readme_issues = check_readme_sections(doc_path)
                report["doc_analysis"]["readme_issues"].extend([
                    {"file": str(doc_path), **issue} for issue in readme_issues
                ])
        except Exception as e:
            print(f"Error analyzing {doc_path}: {e}")

    # Generate recommendations
    if report["code_analysis"]["coverage_percentage"] < CONFIG["min_doc_coverage"]:
        report["recommendations"].append({
            "type": "low_coverage",
            "message": f"Documentation coverage ({report['code_analysis']['coverage_percentage']}%) is below target ({CONFIG['min_doc_coverage']}%)",
            "priority": "high",
        })

    if report["doc_analysis"]["link_issues"]:
        report["recommendations"].append({
            "type": "broken_links",
            "message": f"Found {len(report['doc_analysis']['link_issues'])} broken links",
            "priority": "medium",
        })

    return report


def print_report(report: Dict) -> None:
    """Print a formatted report to stdout."""
    print("=" * 60)
    print("DOCUMENTATION REPORT")
    print("=" * 60)
    print(f"Generated: {report['generated_at']}")
    print(f"Root: {report['root_dir']}")
    print()

    # Code Analysis
    print("CODE DOCUMENTATION COVERAGE")
    print("-" * 40)
    ca = report["code_analysis"]
    print(f"Files analyzed: {ca['total_files']}")
    print(f"Total exports: {ca['total_exports']}")
    print(f"Documented: {ca['documented']}")
    print(f"Undocumented: {ca['undocumented']}")
    print(f"Coverage: {ca['coverage_percentage']}%")
    print()

    if ca["undocumented"] > 0:
        print("Undocumented exports:")
        for file_info in ca["files"]:
            if file_info["undocumented"]:
                print(f"  {file_info['file']}:")
                for name in file_info["undocumented"]:
                    print(f"    - {name}")
        print()

    # Documentation Analysis
    print("DOCUMENTATION FILES")
    print("-" * 40)
    da = report["doc_analysis"]
    print(f"Documentation files: {da['total_files']}")
    print(f"Link issues: {len(da['link_issues'])}")
    print(f"README issues: {len(da['readme_issues'])}")
    print()

    if da["link_issues"]:
        print("Broken links:")
        for issue in da["link_issues"]:
            print(f"  {issue['file']}:{issue['line']} - {issue['url']}")
        print()

    if da["readme_issues"]:
        print("README issues:")
        for issue in da["readme_issues"]:
            severity = "ERROR" if issue["severity"] == "error" else "WARN"
            print(f"  [{severity}] Missing section: {issue['section']}")
        print()

    # Recommendations
    if report["recommendations"]:
        print("RECOMMENDATIONS")
        print("-" * 40)
        for rec in report["recommendations"]:
            print(f"[{rec['priority'].upper()}] {rec['message']}")
        print()

    print("=" * 60)


def save_report(report: Dict, output_path: str) -> None:
    """Save report to a JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"Report saved to: {output_path}")


# ============================================================================
# Main
# ============================================================================

def main():
    """Main entry point."""
    root_dir = sys.argv[1] if len(sys.argv) > 1 else "."

    print(f"Analyzing documentation in: {os.path.abspath(root_dir)}")
    print()

    report = generate_report(root_dir)
    print_report(report)

    # Optionally save JSON report
    if len(sys.argv) > 2:
        save_report(report, sys.argv[2])

    # Exit with error if coverage is below threshold
    if report["code_analysis"]["coverage_percentage"] < CONFIG["min_doc_coverage"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
