# WoV DPS Calculator — Style Reference

> A reusable style guide extracted from the Winds of Valen DPS Calculator.  
> Use this as a foundation for future WoV wiki tools and calculators.

---

## Design Tokens (CSS Custom Properties)

### Backgrounds
| Token | Value | Usage |
|---|---|---|
| `--bg-body` | `#1a1a18` | Page background |
| `--bg-panel` | `#242421` | Card/panel fill |
| `--bg-input` | `#1a1a18` | Input fields, stat rows |
| `--bg-header` | `#1d1d1b` | Panel headers, results table cells |
| `--bg-hover` | `#2e2e2a` | Dropdown option hover |
| `--bg-slot` | `#2a2f2a` | Equipment slot default |
| `--bg-slot-hover` | `#353a35` | Equipment slot hover |
| `--bg-slot-active` | `#3a4035` | Equipment slot active/selected |

### Borders
| Token | Value | Usage |
|---|---|---|
| `--border` | `#3a3a35` | Default borders |
| `--border-light` | `#4a4a42` | Lighter borders, tooltips |
| `--border-slot` | `#4a4a42` | Equipment grid slot borders |

### Accent & Semantic Colors
| Token | Value | Usage |
|---|---|---|
| `--accent` | `#f6931d` | Primary accent — headers, active states, CTA |
| `--accent-hover` | `#ffa940` | Accent on hover |
| `--accent-glow` | `rgba(246,147,29,0.15)` | Subtle accent background |
| `--accent-dim` | `rgba(246,147,29,0.08)` | Very subtle accent tint |
| `--green` | `#5cb85c` | Positive values (DPS, code highlights) |
| `--red` | `#e74c3c` | Negative/danger values (max hit, slash badge) |
| `--blue` | `#5dade2` | Informational values (accuracy, pierce badge) |

### Text
| Token | Value | Usage |
|---|---|---|
| `--text` | `#e8e6e0` | Primary text |
| `--text-dim` | `#9e9c96` | Secondary text (labels, descriptions) |
| `--text-muted` | `#6a6862` | Tertiary text (placeholders, disabled) |

### Other
| Token | Value | Usage |
|---|---|---|
| `--radius` | `6px` | Default border radius for panels |

---

## Typography

### Font Stack
```css
font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
```

### Scale & Weights
| Context | Size | Weight | Extras |
|---|---|---|---|
| Site header `h1` | `1.1rem` | 700 | `letter-spacing: -0.02em`, color: accent |
| Subtitle | `0.78rem` | 400 | color: `--text-dim` |
| Panel header | `0.82rem` | 700 | Uppercase, `letter-spacing: 0.04em` |
| Form label | `0.75rem` | 600 | color: `--text-dim` |
| Input text | `0.8rem` | 400 | — |
| Stat label | `0.75rem` | 500 | color: `--text-dim` |
| Stat value | `0.75rem` | 700 | `font-variant-numeric: tabular-nums` |
| Section title | `0.7rem` | 700 | Uppercase, `letter-spacing: 0.04em`, color: `--text-muted` |
| Badge | `0.65rem` | 700 | Uppercase, `letter-spacing: 0.03em` |
| Results value | `1.1rem` | 800 | `font-variant-numeric: tabular-nums`, `letter-spacing: -0.02em` |
| Results header | `0.7rem` | 600 | Uppercase, `letter-spacing: 0.04em`, color: `--text-dim` |
| Tab | `0.72rem` | 700 | Uppercase, `letter-spacing: 0.04em` |

### Base
```css
html { font-size: 14px; }
body { line-height: 1.5; }
```

---

## Layout

### Main Grid
```css
.main-grid {
  max-width: 1100px;
  margin: 0 auto;
  padding: 1rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
}
```
- **2-column** layout for desktop; collapses to **1-column** at `700px`.
- Full-width elements use `grid-column: 1 / -1`.

### Responsive Breakpoint
```css
@media (max-width: 700px) {
  .main-grid { grid-template-columns: 1fr; }
}
```

---

## Component Patterns

### Panel (`.panel`)
The primary container component. Consists of a header and body.
```css
.panel {
  background: var(--bg-panel);
  border: 1px solid var(--border);
  border-radius: var(--radius);       /* 6px */
  overflow: visible;
}
.panel-header {
  background: var(--bg-header);
  padding: 0.5rem 0.85rem;
  font-size: 0.82rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--accent);
  border-bottom: 1px solid var(--border);
  border-radius: var(--radius) var(--radius) 0 0;
}
.panel-body {
  padding: 0.75rem 0.85rem;
}
```

### Form Row (`.form-row`)
Horizontal label + input layout.
```css
.form-row {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}
.form-row label {
  min-width: 80px;
  flex-shrink: 0;
}
.form-row input, .form-row select {
  flex: 1;
  padding: 0.35rem 0.5rem;
  background: var(--bg-input);
  border: 1px solid var(--border);
  border-radius: 4px;
  color: var(--text);
  font-size: 0.8rem;
  outline: none;
  transition: border-color 0.15s;
}
/* Focus state — accent border, no glow */
.form-row input:focus, .form-row select:focus {
  border-color: var(--accent);
}
/* Hide number spinners */
input[type="number"] { -moz-appearance: textfield; appearance: textfield; }
input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button { -webkit-appearance: none; }
```

### Stat Grid (`.stat-grid`)
Compact key-value display for stats.
```css
.stat-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.3rem;
}
.stat-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.25rem 0.5rem;
  background: var(--bg-input);
  border-radius: 4px;
  font-size: 0.75rem;
}
/* Full-width stat row */
.stat-full { grid-column: 1 / -1; }
```

### Badge
Small inline label for categorical info.
```css
.badge {
  display: inline-block;
  padding: 0.1rem 0.45rem;
  border-radius: 3px;
  font-size: 0.65rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}
/* Variants */
.badge-slash  { background: rgba(231,76,60,0.15);  color: var(--red);  }
.badge-pierce { background: rgba(93,173,226,0.15);  color: var(--blue); }
.badge-none   { background: rgba(158,156,150,0.1);  color: var(--text-muted); }
.badge-boss   { background: var(--accent-dim);       color: var(--accent); }
.badge-mob    { background: rgba(158,156,150,0.08);  color: var(--text-muted); }
```

### Tabs
Horizontal navigation tabs.
```css
.page-tab {
  padding: 0.4rem 1rem;
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--text-muted);
  cursor: pointer;
  border: none;
  background: transparent;
  border-bottom: 2px solid transparent;
  transition: color 0.15s;
}
.page-tab:hover { color: var(--text); }
.page-tab.active {
  color: var(--accent);
  border-bottom-color: var(--accent);
}
```

### Loadout Tabs (Pill Tabs)
Smaller tabs used inside panels for switching content.
```css
.loadout-tab {
  padding: 0.3rem 0.6rem;
  border-radius: 3px;
  font-size: 0.72rem;
  font-weight: 700;
  background: var(--bg-slot);
  border: 1px solid var(--border);
  color: var(--text-muted);
  transition: all 0.15s;
}
.loadout-tab.active {
  background: var(--accent-dim);
  border-color: var(--accent);
  color: var(--accent);
}
/* "Add" button — dashed border variant */
.loadout-add {
  border: 1px dashed var(--border);
  background: transparent;
  color: var(--text-muted);
}
.loadout-add:hover {
  border-color: var(--accent);
  color: var(--accent);
}
```

### Searchable Dropdown
Custom select with search input.
```css
.ss-trigger {
  background: var(--bg-input);
  border: 1px solid var(--border);
  border-radius: 4px;
  color: var(--text);
  font-size: 0.8rem;
  cursor: pointer;
  transition: border-color 0.15s;
}
.ss-trigger.open { border-color: var(--accent); }
.ss-dropdown {
  background: var(--bg-panel);
  border: 1px solid var(--accent);
  border-radius: 4px;
  box-shadow: 0 6px 24px rgba(0,0,0,0.5);
  max-height: 260px;
}
.ss-option:hover { background: var(--bg-hover); }
.ss-option.selected { background: var(--accent-dim); color: var(--accent); }
```

### Results Table
Full-width tabular results display.
```css
.results-table th {
  background: var(--bg-panel);
  color: var(--text-dim);
  font-weight: 600;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.results-table td {
  font-weight: 800;
  font-size: 1.1rem;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
  color: var(--text);
  background: var(--bg-header);
}
/* Semantic cell colors */
.r-accuracy { color: var(--blue)  !important; }
.r-maxhit   { color: var(--red)   !important; }
.r-dps      { color: var(--green) !important; }
.r-ttk      { color: var(--accent)!important; }
```

### Disclaimer / Warning Banner
```css
/* Inline style pattern used for warnings */
{
  margin-top: 0.5rem;
  padding: 0.5rem 0.75rem;
  background: #3a2a10;
  border: 1px solid #6b4f1d;
  border-radius: 4px;
  font-size: 0.72rem;
  color: #e8c56d;
}
```

### Chart Controls
```css
.chart-controls label {
  font-size: 0.7rem;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.chart-controls select {
  background: var(--bg-input);
  border: 1px solid var(--border);
  color: var(--text);
  padding: 0.25rem 0.4rem;
  border-radius: 3px;
  font-size: 0.75rem;
}
```

### Tooltip
```css
.chart-tooltip {
  background: rgba(30,30,28,0.95);
  border: 1px solid var(--border-light);
  border-radius: 4px;
  padding: 0.4rem 0.55rem;
  font-size: 0.7rem;
  color: var(--text);
  box-shadow: 0 2px 8px rgba(0,0,0,0.4);
}
```

---

## Site Header

```css
.site-header {
  background: var(--bg-header);
  border-bottom: 2px solid var(--accent);
  padding: 0.6rem 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
```
- Title in accent color, subtitle in `--text-dim`.
- Page tabs aligned to the right with `margin-left: auto`.
- Version number in `--text-muted` at `0.6rem`.

---

## Equipment Grid (Visual Inventory)

```css
.equip-visual {
  display: grid;
  grid-template-columns: repeat(3, 80px);
  grid-template-rows: repeat(4, 80px);
  gap: 4px;
  justify-content: center;
}
.eslot {
  width: 80px; height: 80px;
  background: var(--bg-slot);
  border: 2px solid var(--border-slot);
  border-radius: 4px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: border-color 0.15s, background 0.15s;
}
.eslot:hover { border-color: var(--text-muted); background: var(--bg-slot-hover); }
.eslot.active { border-color: var(--accent); background: var(--bg-slot-active); }
.eslot.disabled { opacity: 0.3; pointer-events: none; }
```
- Slots shrink to `70px` at `≤700px`.
- Slot icons are `48px` at `0.25` opacity; `1.0` opacity when an item is equipped.
- Slot labels positioned at `.slot-label { position: absolute; bottom: 2px; }`.

---

## Collapsible Sections (Methodology)

```css
.methodology details {
  background: var(--bg-panel);
  border: 1px solid var(--border);
  border-radius: var(--radius);
}
.methodology summary {
  padding: 0.6rem 0.85rem;
  font-size: 0.82rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--accent);
  cursor: pointer;
  background: var(--bg-header);
  list-style: none;
}
/* Custom triangle indicator */
summary::before { content: '▶  '; font-size: 0.6rem; }
details[open] summary::before { transform: rotate(90deg); }
```

---

## Conventions & Patterns

### Spacing
- Panel body padding: `0.75rem 0.85rem`
- Section dividers: `<hr class="section-divider">` with `margin: 0.6rem 0`
- Form row gap: `0.5rem`
- Stat grid gap: `0.3rem`

### Transitions
- Default: `0.15s` on `border-color`, `background`, `color`
- No easing function specified (uses browser default)

### Focus States
- Inputs use `border-color: var(--accent)` on focus — no box-shadow glow

### Number Display
- Always use `font-variant-numeric: tabular-nums` for numeric values
- Use `letter-spacing: -0.02em` for large result numbers

### Labels & Section Titles
- Always **uppercase** + `letter-spacing: 0.04em`
- Color: `--text-dim` for labels, `--text-muted` for section titles, `--accent` for panel headers

### Color Semantics
| Color | Meaning |
|---|---|
| Accent (`#f6931d`) | Primary actions, active state, headers, TTK |
| Green (`#5cb85c`) | Positive results (DPS), code highlights |
| Red (`#e74c3c`) | Negative/dangerous (max hit, slash type) |
| Blue (`#5dade2`) | Informational (accuracy, pierce type) |
| `--text-muted` | Disabled/neutral states |

### CSS Reset
```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
```
