# DarkSwarm Brand Guide

This short guide contains the brand palette and usage examples for DarkSwarm.

Palette
- Primary (deep base): #0E0F1A — deep near-black for backgrounds and primary text on light backgrounds
- Accent / Brand: #7C4DFF — electric violet (primary accent)
- Highlight / Action: #00D4FF — cyan (links, interactive elements)
- Success / Positive: #8CE15B — lime green
- Warning / Accent-2: #FFB86B — warm orange
- Muted text / borders: #9AA4B2 — cool gray
- Surface / light background: #F8FAFC — near-white

CSS variables (example)

```css
:root {
  --ds-bg: #0E0F1A;
  --ds-accent: #7C4DFF;
  --ds-highlight: #00D4FF;
  --ds-success: #8CE15B;
  --ds-warn: #FFB86B;
  --ds-muted: #9AA4B2;
  --ds-surface: #F8FAFC;
}
```

Logo usage
- Use `assets/logo.svg` for the primary mark.
- Use the accent gradient for large displays and the flat violet for small icons.

README header and social preview
- `assets/banner.svg` is the scalable hero banner used at the top of README.md.
- Add a social preview image (.github/social-preview.svg or .png) exported from the banner for link sharing.

Accessibility
- Ensure color contrast for small text meets WCAG 2.1 AA (4.5:1).
- For badges and small UI, prefer white text on accent background.

Examples
- Callout box style:

```css
.callout {
  background: rgba(124,77,255,0.06);
  border-left: 4px solid #7C4DFF;
  padding: 12px;
}
```

Assets added in this change
- assets/banner.svg
- assets/logo.svg
- assets/terminal-demo.svg (recolored)
- docs/brand.md

