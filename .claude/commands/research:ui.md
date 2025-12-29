# Research UI

Research UI design from Figma: $ARGUMENTS

## Overview

This command orchestrates comprehensive UI/UX research from Figma designs. It extracts visual assets, analyzes layouts using AI vision, and produces detailed design documentation for implementation guidance.

**IMPORTANT**: This command is for **research and documentation only**. It does not implement, plan, or write code. The output is a comprehensive design specification document.

---

## Prerequisites

Before running this command, ensure:

1. **Figma Access Token** is configured:
   ```bash
   export FIGMA_ACCESS_TOKEN="your-figma-token"
   ```

2. **Gemini API Key** is configured:
   ```bash
   export GEMINI_API_KEY="your-gemini-key"
   ```

3. **Dependencies** are installed:
   ```bash
   pip install requests python-dotenv google-genai pillow
   ```

---

## Execution Flow

### 1. Initialize Research Session

Create session directory:
```
plans/research/ui/{date}-{design-slug}/
├── README.md              # Overview and quick reference
├── assets/                # Exported design images
│   ├── design.png         # Main design export
│   └── components/        # Individual component exports
├── figma-metadata.json    # Raw Figma API response
├── layout-analysis.md     # Layout structure analysis
├── design-tokens.md       # Extracted design tokens
├── design-tokens.css      # CSS custom properties
├── components.md          # Component specifications
├── generated-styles.css   # Generated CSS code
└── implementation-notes.md # Developer notes
```

### 2. Parse Figma URL

Extract from the provided Figma URL:
- File key
- Node ID (if specific frame/component)
- File name

Validate URL format:
```
https://www.figma.com/file/{key}/{name}?node-id={id}
https://www.figma.com/design/{key}/{name}?node-id={id}
```

### 3. Export Design Assets

**Invoke figma-analyzer skill:**

```bash
python .claude/skills/figma-analyzer/scripts/figma_export.py \
  --url "$FIGMA_URL" \
  --output plans/research/ui/{session}/assets/design.png \
  --scale 2 \
  --verbose
```

**Also fetch metadata:**

```bash
python .claude/skills/figma-analyzer/scripts/figma_export.py \
  --url "$FIGMA_URL" \
  --metadata-only \
  --output plans/research/ui/{session}/figma-metadata.json
```

### 4. Visual Layout Analysis

**CRITICAL: Use ai-multimodal skill for ALL visual analysis**

Never use Claude's default vision. Always invoke the Gemini-based ai-multimodal skill.

```bash
python .claude/skills/ai-multimodal/scripts/gemini_batch_process.py \
  --files plans/research/ui/{session}/assets/design.png \
  --task analyze \
  --prompt "Analyze this UI design comprehensively:

## Layout Structure
1. Identify the overall layout pattern (grid, flexbox, single column, multi-column)
2. Map the visual hierarchy and section organization
3. Document header, main content, sidebar, footer areas
4. Identify responsive breakpoint hints from the design

## Component Hierarchy
1. List all identifiable UI components
2. Document parent-child relationships
3. Identify repeated patterns and component variants
4. Note interactive elements (buttons, inputs, links)

## Visual Groupings
1. Identify content sections and their purposes
2. Document spacing patterns between groups
3. Note visual separators (lines, shadows, whitespace)

## Navigation & Information Architecture
1. Document navigation elements
2. Identify breadcrumbs, tabs, or other wayfinding
3. Note content organization patterns

Return as structured markdown with clear headings." \
  --output plans/research/ui/{session}/layout-analysis.md \
  --model gemini-2.5-flash
```

### 5. Design Token Extraction

```bash
python .claude/skills/ai-multimodal/scripts/gemini_batch_process.py \
  --files plans/research/ui/{session}/assets/design.png \
  --task analyze \
  --prompt "Extract all design tokens from this UI design:

## Color Palette
For each color identified:
- Hex value
- RGB/HSL value
- Usage context (primary, secondary, background, text, accent, etc.)
- Contrast ratio notes for accessibility

## Typography
For each text style:
- Font family (identify or describe)
- Font size (estimate in px)
- Font weight (100-900)
- Line height
- Letter spacing
- Text color
- Usage (headings, body, captions, etc.)

## Spacing System
- Identify the spacing scale used
- Document margin patterns
- Document padding patterns
- Note any 4px, 8px, or other base unit

## Border Styles
- Border radius values
- Border widths
- Border colors

## Shadow Styles
- Box shadow definitions
- Usage context

## Icon Styles
- Icon sizes
- Icon colors
- Icon stroke widths

Format output as both:
1. A human-readable specification table
2. CSS custom properties code block" \
  --output plans/research/ui/{session}/design-tokens.md \
  --model gemini-2.5-flash
```

### 6. Component Specification

```bash
python .claude/skills/ai-multimodal/scripts/gemini_batch_process.py \
  --files plans/research/ui/{session}/assets/design.png \
  --task analyze \
  --prompt "Document detailed specifications for each UI component:

For EACH component identified, provide:

## Component: [Name]
### Type
- Category (button, input, card, navigation, etc.)

### Visual Description
- Appearance and styling details

### States (if applicable)
- Default state
- Hover state indicators
- Active/pressed state
- Disabled state
- Focus state

### Content Structure
- Text content and formatting
- Icons present
- Images or media
- Nested components

### Dimensions
- Width (fixed, fluid, or range)
- Height
- Padding
- Margin

### Styling
- Background
- Borders
- Shadows
- Typography used

### Interaction Patterns
- Click/tap behavior expected
- Hover effects suggested
- Transitions/animations visible

### Accessibility Notes
- Color contrast observations
- Touch target size
- Label requirements

Return as detailed component specification cards." \
  --output plans/research/ui/{session}/components.md \
  --model gemini-2.5-flash
```

### 7. CSS Code Generation

```bash
python .claude/skills/ai-multimodal/scripts/gemini_batch_process.py \
  --files plans/research/ui/{session}/assets/design.png \
  --task analyze \
  --prompt "Generate production-ready CSS code based on this design:

## CSS Custom Properties
Create a complete :root block with:
- Color tokens (--color-*)
- Typography tokens (--font-*, --text-*)
- Spacing tokens (--space-*)
- Border tokens (--border-*, --radius-*)
- Shadow tokens (--shadow-*)
- Transition tokens (--transition-*)

## Base Styles
- Reset/normalize essentials
- Body defaults
- Container classes
- Typography base styles

## Component Classes
For each visible component, create:
- Base class with all styling
- Modifier classes for variants
- State classes (hover, active, disabled)

## Layout Classes
- Grid/flexbox utilities
- Spacing utilities
- Responsive breakpoints

## Dark Mode (if indicators visible)
- Alternative color scheme
- @media (prefers-color-scheme: dark) block

Use modern CSS:
- CSS custom properties
- CSS Grid and Flexbox
- clamp() for fluid typography
- :is(), :where() for efficiency

Output as valid, well-commented CSS code." \
  --output plans/research/ui/{session}/generated-styles.css \
  --model gemini-2.5-flash
```

### 8. Generate Implementation Notes

Create `implementation-notes.md` with:
- Recommended frontend framework/approach
- Component library suggestions
- Critical implementation considerations
- Accessibility checklist
- Responsive design strategy
- Animation/interaction recommendations

### 9. Generate README Summary

Compile all findings into `README.md`:

```markdown
# UI Research: {Design Name}

**Figma Link**: {url}
**Analyzed**: {date}
**Session**: {session-id}

## Design Overview
[Brief description of the design]

## Quick Reference

### Color Palette
[Summary table of main colors]

### Typography Scale
[Summary table of text styles]

### Components Identified
[Numbered list of components]

## Files in This Research

| File | Description |
|------|-------------|
| [layout-analysis.md](./layout-analysis.md) | Layout structure and hierarchy |
| [design-tokens.md](./design-tokens.md) | Extracted design tokens |
| [design-tokens.css](./design-tokens.css) | CSS custom properties |
| [components.md](./components.md) | Component specifications |
| [generated-styles.css](./generated-styles.css) | Generated CSS code |
| [implementation-notes.md](./implementation-notes.md) | Developer notes |

## Next Steps
1. Review design tokens and adjust as needed
2. Validate color contrast for accessibility
3. Confirm component specifications with design team
4. Use generated CSS as starting point for implementation

---
Generated by UI Research workflow using ai-multimodal skill.
```

---

## Skills Used

### figma-analyzer
**Purpose**: Extract design assets from Figma API
**Location**: `.claude/skills/figma-analyzer/SKILL.md`

### ai-multimodal
**Purpose**: Visual analysis using Gemini Vision API
**Location**: `.claude/skills/ai-multimodal/SKILL.md`

**CRITICAL**: All visual analysis MUST use ai-multimodal skill. Never analyze images with Claude's default vision.

---

## Sub-Agent

This command delegates to the **ui-researcher** agent:

**Location**: `.claude/agents/research/ui-researcher.md`

The agent orchestrates:
1. Figma asset extraction
2. Multi-pass visual analysis
3. Design token extraction
4. Documentation generation

---

## Error Handling

| Error | Resolution |
|-------|------------|
| Missing FIGMA_ACCESS_TOKEN | Prompt user to set token |
| Missing GEMINI_API_KEY | Prompt user to set API key |
| Invalid Figma URL | Show correct URL format |
| Figma API 403 | Token invalid or file not accessible |
| Figma API 404 | File or node not found |
| Gemini API error | Check API key and quota |
| Image too large | Suggest using --scale 1 |

---

## Output Quality Gates

Before completing, verify:
- [ ] Design image exported successfully
- [ ] Figma metadata captured
- [ ] Layout analysis complete
- [ ] Design tokens extracted
- [ ] CSS custom properties generated
- [ ] Component specs documented
- [ ] Generated CSS created
- [ ] README summary compiled

---

## Example Usage

```bash
# Research a specific Figma frame
/research:ui https://www.figma.com/file/ABC123/MyDesign?node-id=1-234

# Research an entire Figma page
/research:ui https://www.figma.com/file/ABC123/MyDesign

# With additional context
/research:ui https://www.figma.com/file/ABC123/Dashboard - Focus on the analytics cards and data visualization components
```

---

## Constraints

1. **Research only** - No implementation or planning
2. **ai-multimodal only** - Never use default Claude vision
3. **Comprehensive** - Capture all visible design details
4. **Structured output** - Consistent formatting across all files
5. **No assumptions** - Document only what is visually present

---

## Phase Indicator

- 🎨 Research UI Design

---

## Completion

When research is complete:
1. Verify all output files exist
2. Review README for completeness
3. Present summary to user with file locations
4. Suggest next steps (implementation planning)

```
✅ UI Research Complete

Session: plans/research/ui/{session}/

Files Generated:
- README.md - Overview and quick reference
- layout-analysis.md - Layout structure
- design-tokens.md - Design tokens specification
- design-tokens.css - CSS custom properties
- components.md - Component specifications
- generated-styles.css - Generated CSS code
- implementation-notes.md - Developer notes

Next: Review the generated documentation and use /research:codebase or /start for implementation planning.
```

---

## Related Commands

- `/research:codebase` - Research codebase for implementation
- `/research:docs` - Research external documentation and libraries
- `/execute` - Implement the approved plan
- `/code-check` - Validate implementation
