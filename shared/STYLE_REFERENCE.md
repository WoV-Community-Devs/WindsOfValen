# WoV — Style Reference

> A reusable style guide for Winds of Valen wiki tools and pages.  
> Based on the forest/medieval theme with living background effects.

---

## Design Tokens (CSS Custom Properties)

### Backgrounds
| Token | Value | Usage |
|---|---|---|
| `--bg-body` | `#1e2830` | Page background |
| `--bg-panel` | `rgba(30, 40, 48, 0.88)` | Card/panel fill (translucent for blur effect) |
| `--bg-input` | `rgba(24, 32, 40, 0.75)` | Input fields, stat rows |
| `--bg-header` | `rgba(28, 38, 46, 0.92)` | Panel headers, results table cells |
| `--bg-hover` | `rgba(55, 72, 60, 0.5)` | Dropdown option hover |
| `--bg-slot` | `rgba(38, 50, 44, 0.74)` | Equipment slot default |
| `--bg-slot-hover` | `rgba(48, 64, 54, 0.8)` | Equipment slot hover |
| `--bg-slot-active` | `rgba(58, 82, 64, 0.84)` | Equipment slot active/selected |

### Borders
| Token | Value | Usage |
|---|---|---|
| `--border` | `rgba(100, 116, 90, 0.58)` | Default borders |
| `--border-light` | `rgba(125, 142, 112, 0.58)` | Lighter borders, tooltips |
| `--border-slot` | `rgba(100, 116, 90, 0.52)` | Equipment grid slot borders |

### Accent & Semantic Colors
| Token | Value | Usage |
|---|---|---|
| `--accent` | `#d4a843` | Primary accent — headers, active states, CTA |
| `--accent-hover` | `#e8c060` | Accent on hover |
| `--accent-glow` | `rgba(212,168,67,0.2)` | Subtle accent glow |
| `--accent-dim` | `rgba(212,168,67,0.1)` | Very subtle accent tint |
| `--green` | `#6abf69` | Positive values (DPS) |
| `--red` | `#c9503a` | Negative/danger values (max hit, slash badge) |
| `--blue` | `#5ba8c8` | Informational values (accuracy, pierce badge) |

### Text
| Token | Value | Usage |
|---|---|---|
| `--text` | `#e8e4d2` | Primary text |
| `--text-dim` | `#b8ae98` | Secondary text (labels, descriptions) |
| `--text-muted` | `#9a9280` | Tertiary text (section titles, placeholders) |

### Other
| Token | Value | Usage |
|---|---|---|
| `--radius` | `4px` | Default border radius for panels |
| `--panel-shadow` | `0 4px 24px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.04)` | Panel box shadow |

---

## Typography

### Font Stack
```css
/* Body text */
font-family: 'Crimson Text', 'Segoe UI', Georgia, serif;
/* Headings, labels, panel headers */
font-family: 'Cinzel', serif;
```

**Google Fonts import:**
```html
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Crimson+Text:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
```

### Scale & Weights
| Context | Font | Size | Weight | Extras |
|---|---|---|---|---|
| Site header `h1` | Cinzel | `1.2rem` | 900 | `letter-spacing: 0.06em`, text-shadow glow |
| Subtitle | Cinzel | `0.78rem` | 400 | color: `--text-dim`, `letter-spacing: 0.04em` |
| Panel header | Cinzel | `0.82rem` | 700 | Uppercase, `letter-spacing: 0.06em`, text-shadow |
| Form label | Cinzel | `0.72rem` | 700 | color: `--text-dim`, `letter-spacing: 0.03em` |
| Input text | Crimson Text | `0.8rem` | 400 | — |
| Stat label | Cinzel | `0.68rem` | 700 | color: `--text-dim`, `letter-spacing: 0.02em` |
| Stat value | Crimson Text | `0.75rem` | 700 | `font-variant-numeric: tabular-nums` |
| Section title | Cinzel | `0.7rem` | 700 | Uppercase, `letter-spacing: 0.04em`, color: `--text-muted` |
| Badge | Cinzel | `0.62rem` | 700 | Uppercase, `letter-spacing: 0.04em` |
| Results value | Crimson Text | `1.1rem` | 800 | `font-variant-numeric: tabular-nums`, `letter-spacing: -0.02em` |
| Results header | Cinzel | `0.68rem` | 700 | Uppercase, `letter-spacing: 0.06em` |
| Tab | Cinzel | `0.7rem` | 700 | Uppercase, `letter-spacing: 0.06em` |
| Slot label | Cinzel | `0.52rem` | 700 | Uppercase, `letter-spacing: 0.06em` |
| Chart select | Crimson Text | `0.75rem` | 400 | `backdrop-filter: blur(4px)` |

### Base
```css
html { font-size: 14px; }
body { line-height: 1.5; }
```

---

## Living Background

The page uses a fixed background scene with animated particles layered below all content.

### Structure
```html
<div id="bg-scene">
  <div class="bg-gradient"></div>   <!-- Forest-toned radial gradients -->
  <div class="bg-texture"></div>    <!-- Subtle cobblestone texture -->
  <div class="bg-vignette"></div>   <!-- Edge darkening -->
  <div class="water-layer"></div>   <!-- Shimmering water at bottom -->
</div>
```

### Particles (generated via JavaScript)
| Element | Count | Effect |
|---|---|---|
| `.firefly` | 35 | Drifting glowing orbs with pulsing glow |
| `.dust-mote` | 15 | Floating upward particles |
| `.water-ripple` | Dynamic | Ripple circles at bottom (created/removed on interval) |

### Key Animations
| Animation | Duration | Purpose |
|---|---|---|
| `fireflyDrift` | 8–20s | Random drift movement |
| `fireflyGlow` | 2s | Subtle pulsing glow (low intensity) |
| `waterShimmer` | 8s | Gradient position shift |
| `waterRipple` | 4s | Expanding/fading ripple |
| `floatParticle` | 15–40s | Upward float with rotation |

### Content z-index
All content must sit above the background:
```css
.page-view, .methodology, .site-footer, #share-toast {
  position: relative;
  z-index: 2;
}
```

> **Note:** `.site-header` is excluded from this rule — it uses `position: sticky` (see Header section below).

### Sticky Header
The site header must be sticky on **all** pages so the "Back to Home Page" link is always accessible:
```css
.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: linear-gradient(180deg, rgba(15,20,15,0.98), rgba(12,18,14,0.95));
  /* ... other header styles ... */
}
```
Do **not** include `.site-header` in any combined `position: relative` rules, as this will override the sticky behavior.

---

## Visual Effects

### Backdrop Filter
Applied to panels, inputs, dropdowns, and tooltips for glassmorphism:
```css
.panel          { backdrop-filter: blur(10px); }
.eslot          { backdrop-filter: blur(6px);  }
.form-row input { backdrop-filter: blur(4px);  }
.slot-picker    { backdrop-filter: blur(12px); }
.chart-tooltip  { backdrop-filter: blur(8px);  }
```

### Text Shadows (Glow)
Accent-colored elements get a subtle glow:
```css
/* Header title */
text-shadow: 0 0 20px rgba(212,168,67,0.3);
/* Panel headers */
text-shadow: 0 0 12px rgba(212,168,67,0.2);
/* Result values — color-matched */
.r-accuracy { text-shadow: 0 0 8px rgba(91,168,200,0.2); }
.r-dps      { text-shadow: 0 0 8px rgba(106,191,105,0.2); }
.r-maxhit   { text-shadow: 0 0 8px rgba(201,80,58,0.2); }
.r-ttk      { text-shadow: 0 0 8px rgba(212,168,67,0.2); }
```

### Box Shadows
```css
/* Panels */
box-shadow: 0 4px 24px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.04);
/* Header */
box-shadow: 0 2px 20px rgba(0,0,0,0.5), inset 0 -1px 0 rgba(212,168,67,0.15);
/* Active slots */
box-shadow: 0 0 16px rgba(212,168,67,0.2);
/* Active tabs */
box-shadow: 0 0 10px rgba(212,168,67,0.12);
```

### Gradient Backgrounds
```css
/* Site header (higher opacity for sticky scroll) */
background: linear-gradient(180deg, rgba(15,20,15,0.98), rgba(12,18,14,0.95));
/* Panel headers */
background: linear-gradient(180deg, rgba(20,28,22,0.9), rgba(15,22,18,0.85));
/* Results panel header (golden) */
background: linear-gradient(135deg, rgba(180,140,40,0.9), rgba(160,120,30,0.85), rgba(140,100,25,0.9));
/* Equipment slots */
background: linear-gradient(135deg, rgba(25,35,30,0.75), rgba(20,30,25,0.65));
```

---

## Component Patterns

### Site Header (`.site-header`)
The header uses `display:flex` with `position:relative`. The "Back to Home Page" link is **absolutely positioned** at the horizontal center of the header, independent of the left-aligned title and subtitle.
```css
.site-header {
  position: relative;
  display: flex; align-items: center; gap: 0.75rem;
  background: linear-gradient(180deg, rgba(15,20,15,0.95), rgba(12,18,14,0.92));
  border-bottom: 2px solid var(--accent);
  padding: 0.6rem 1.5rem;
  backdrop-filter: blur(10px);
}
.home-link {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  font-family: 'Cinzel', serif;
  font-size: 0.85rem; font-weight: 700;
  color: var(--accent);
}
```

### Panel (`.panel`)
```css
.panel {
  background: var(--bg-panel);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: visible;
  backdrop-filter: blur(10px);
  box-shadow: var(--panel-shadow);
}
.panel-header {
  background: linear-gradient(180deg, rgba(20,28,22,0.9), rgba(15,22,18,0.85));
  padding: 0.5rem 0.85rem;
  font-family: 'Cinzel', serif;
  font-size: 0.82rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.06em;
  color: var(--accent);
  border-bottom: 1px solid var(--border);
  text-shadow: 0 0 12px rgba(212,168,67,0.2);
}
```

### Form Row (`.form-row`)
```css
.form-row input, .form-row select {
  flex: 1;
  padding: 0.35rem 0.5rem;
  background: var(--bg-input);
  border: 1px solid var(--border);
  border-radius: 3px;
  color: var(--text);
  font-size: 0.8rem;
  transition: border-color 0.2s, box-shadow 0.2s;
  backdrop-filter: blur(4px);
}
.form-row input:focus, .form-row select:focus {
  border-color: var(--accent);
  box-shadow: 0 0 8px rgba(212,168,67,0.15);
}
```

### Badge
```css
.badge {
  font-family: 'Cinzel', serif;
  font-size: 0.62rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.04em;
}
.badge-slash  { background: rgba(201,80,58,0.18);  color: var(--red);  border: 1px solid rgba(201,80,58,0.2); }
.badge-pierce { background: rgba(91,168,200,0.15);  color: var(--blue); border: 1px solid rgba(91,168,200,0.2); }
.badge-boss   { background: var(--accent-dim); color: var(--accent); border: 1px solid rgba(212,168,67,0.2); text-shadow: 0 0 8px rgba(212,168,67,0.3); }
```

### Searchable Dropdown
```css
.ss-trigger {
  backdrop-filter: blur(4px);
  transition: border-color 0.2s, box-shadow 0.2s;
}
.ss-trigger.open { box-shadow: 0 0 10px rgba(212,168,67,0.12); }
.ss-dropdown {
  background: rgba(15,20,16,0.95);
  border: 1px solid var(--accent);
  box-shadow: 0 6px 24px rgba(0,0,0,0.6), 0 0 16px rgba(212,168,67,0.06);
  backdrop-filter: blur(12px);
}
```

### Results Table
```css
.results-panel .panel-header {
  background: linear-gradient(135deg, rgba(180,140,40,0.9), rgba(160,120,30,0.85), rgba(140,100,25,0.9));
  color: #0d1117;
  font-family: 'Cinzel', serif; font-size: 0.85rem; font-weight: 900;
  text-shadow: 0 1px 2px rgba(255,255,255,0.1);
}
.results-table thead th {
  background: rgba(18,24,20,0.85);
  font-family: 'Cinzel', serif;
}
.results-table tbody td {
  background: rgba(15,20,16,0.7);
}
```

---

## Conventions & Patterns

### Transitions
- Default: `0.2s` on `border-color`, `background`, `color`, `box-shadow`
- Use `transition: all 0.2s` for interactive elements (tabs, buttons)

### Focus & Active States
- Inputs: `border-color: var(--accent)` + `box-shadow: 0 0 8px rgba(212,168,67,0.15)`
- Slots: `box-shadow: 0 0 16px rgba(212,168,67,0.2)`
- Tabs: `box-shadow: 0 0 10px rgba(212,168,67,0.12)`

### Fonts Rule of Thumb
- **Cinzel** for all headings, labels, panel headers, badges, tabs — anything structural
- **Crimson Text** for body content, input values, result numbers — anything readable

### Color Semantics
| Color | Meaning |
|---|---|
| Accent (`#d4a843`) | Primary actions, active state, headers, TTK |
| Green (`#6abf69`) | Positive results (DPS) |
| Red (`#c9503a`) | Negative/danger (max hit, slash type) |
| Blue (`#5ba8c8`) | Informational (accuracy, pierce type) |
| `--text-muted` | Disabled/neutral states |

### Emoji Usage
- **Minimal emoji use.** Avoid emojis in headings, tabs, buttons, and labels. The medieval/fantasy theme relies on typography and color for visual hierarchy, not emoji icons.
- Emojis are acceptable only as small decorative elements in the index page data chips (e.g. the Game Data grid), where they serve as compact category indicators.

### Methodology Sections
- Use `<details open>` so all sections start expanded
- Arrow indicator uses `::before` pseudo-element with `margin-right: 0.5rem`
- Summary text uses Cinzel, uppercase, accent color with text-shadow glow
