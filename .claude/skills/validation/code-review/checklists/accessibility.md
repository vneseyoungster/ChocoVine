# Accessibility (a11y) Review Checklist

## Semantic HTML

### Document Structure
- [ ] Proper heading hierarchy (h1 → h2 → h3)
- [ ] Only one h1 per page
- [ ] Landmarks used (main, nav, aside, footer)
- [ ] Page has meaningful title

### Interactive Elements
- [ ] Buttons for actions (not div/span)
- [ ] Links for navigation (not buttons)
- [ ] Form inputs have associated labels
- [ ] Fieldsets for grouped inputs

### Content Structure
- [ ] Lists use ul/ol/dl elements
- [ ] Tables have headers (th) and scope
- [ ] Data tables have captions
- [ ] Proper use of article, section, aside

## Keyboard Navigation

### Focus Management
- [ ] All interactive elements focusable
- [ ] Focus order is logical (tab order)
- [ ] Focus visible on all elements
- [ ] No focus traps (except modals)

### Keyboard Interaction
- [ ] Enter/Space activate buttons
- [ ] Escape closes modals/popups
- [ ] Arrow keys work in menus/lists
- [ ] Skip links provided for navigation

### Custom Components
- [ ] Custom controls keyboard accessible
- [ ] Keyboard shortcuts documented
- [ ] No mouse-only interactions
- [ ] Touch targets large enough (44x44px)

## ARIA Usage

### ARIA Labels
- [ ] aria-label for icon buttons
- [ ] aria-labelledby for sections
- [ ] aria-describedby for instructions
- [ ] aria-hidden for decorative content

### ARIA Roles
- [ ] Correct roles for custom widgets
- [ ] role="button" for clickable non-buttons
- [ ] role="alert" for important messages
- [ ] role="dialog" for modals

### ARIA States
- [ ] aria-expanded for collapsibles
- [ ] aria-selected for tabs/options
- [ ] aria-checked for checkboxes
- [ ] aria-disabled for disabled elements

### ARIA Live Regions
- [ ] aria-live for dynamic content
- [ ] Appropriate politeness level
- [ ] aria-atomic when needed
- [ ] Status messages announced

## Visual Design

### Color Contrast
- [ ] Text contrast ratio >= 4.5:1 (normal text)
- [ ] Text contrast ratio >= 3:1 (large text)
- [ ] UI element contrast >= 3:1
- [ ] Focus indicator contrast sufficient

### Color Independence
- [ ] Color not sole indicator of state
- [ ] Error states have text/icon indicators
- [ ] Links distinguishable without color
- [ ] Charts have patterns, not just colors

### Text & Typography
- [ ] Text resizable to 200% without breaking
- [ ] Line height >= 1.5 for body text
- [ ] Paragraph spacing sufficient
- [ ] No justified text alignment

### Motion & Animation
- [ ] Prefers-reduced-motion respected
- [ ] No auto-playing video/audio
- [ ] Animation can be paused
- [ ] No flashing content (> 3 flashes/sec)

## Forms

### Labels & Instructions
- [ ] All inputs have visible labels
- [ ] Required fields indicated
- [ ] Input format requirements shown
- [ ] Help text accessible

### Error Handling
- [ ] Error messages clear and helpful
- [ ] Errors associated with inputs
- [ ] Error summary at form top
- [ ] Focus moves to error on submit

### Form Controls
- [ ] Autocomplete attributes set
- [ ] Input types appropriate (email, tel, etc.)
- [ ] Select has default option
- [ ] Radio/checkbox groups labeled

## Images & Media

### Images
- [ ] Alt text for informative images
- [ ] Alt="" for decorative images
- [ ] Complex images have long description
- [ ] Text in images avoided

### Video/Audio
- [ ] Captions for video
- [ ] Transcripts available
- [ ] Audio descriptions when needed
- [ ] Media player accessible

## Screen Reader Testing

### Content Announcements
- [ ] Page title announced on load
- [ ] Dynamic content changes announced
- [ ] Loading states communicated
- [ ] Error/success messages read

### Navigation
- [ ] Skip to content link works
- [ ] Landmarks navigable
- [ ] Heading navigation works
- [ ] Forms navigable by input

## Common Issues to Flag

### Critical
```
Issue: Missing form labels
<input type="text" placeholder="Email">
Fix: <label for="email">Email</label><input id="email" type="text">

Issue: Non-focusable interactive element
<div onclick="submit()">Submit</div>
Fix: <button onclick="submit()">Submit</button>

Issue: Missing alt text
<img src="chart.png">
Fix: <img src="chart.png" alt="Sales chart showing 20% growth">

Issue: Color-only indication
<span style="color: red">Error</span>
Fix: <span style="color: red" role="alert">❌ Error: Required field</span>
```

### Warnings
```
Issue: Poor focus visibility
:focus { outline: none; }
Fix: :focus { outline: 2px solid blue; outline-offset: 2px; }

Issue: Missing skip link
Fix: <a href="#main" class="skip-link">Skip to content</a>

Issue: Non-descriptive link text
<a href="...">Click here</a>
Fix: <a href="...">View full report</a>
```

## Testing Tools

### Automated
- axe DevTools
- WAVE
- Lighthouse accessibility audit
- eslint-plugin-jsx-a11y

### Manual Testing
- Keyboard-only navigation
- Screen reader (VoiceOver, NVDA, JAWS)
- Browser zoom to 200%
- Windows High Contrast mode

## WCAG Level Reference

### Level A (Minimum)
- All images have alt text
- Keyboard accessible
- No flashing content
- Bypass blocks available

### Level AA (Standard)
- Color contrast met
- Text resizable
- Focus visible
- Error identification

### Level AAA (Enhanced)
- Higher contrast ratios
- Extended audio descriptions
- Sign language
- Reading level
