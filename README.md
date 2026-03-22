# ⚔️ Winds of Valen — Community Database & Tools

A community-driven collection of game data, interactive tools, and formula documentation for [Winds of Valen](https://store.steampowered.com/app/Winds_of_Valen).

> **Live Site:** Hosted via GitHub Pages — open `index.html` to browse all tools.

---

## 🗂️ Project Structure

```
WindsOfValen/
├── index.html                  # Landing page with links to all tools
├── data/
│   ├── WoV_Data_Browser.html   # Interactive item/entity browser
│   ├── entities/               # Game item data (JSON)
│   └── npcs/                   # Monster & boss data (JSON)
├── tools/
│   ├── DPS Calculator/         # Damage-per-second calculator
│   └── XP Calculator/          # Experience rate calculator
├── formulas/
│   ├── WoV_Formulas.html       # Interactive formula reference page
│   ├── damage.md               # Damage calculation breakdown
│   ├── experience.md           # XP formula documentation
│   └── sell_price.md           # Sell price formula (70% of buy price)
├── icons/
│   └── items/                  # Item icon sprites (94×95 PNG)
└── shared/
    └── STYLE_REFERENCE.md      # UI design system & style guide
```

---

## 🛠️ Tools

### [Data Browser](data/WoV_Data_Browser.html)
Interactive, searchable browser for all game entities. Displays item stats, descriptions, icons, prices, crafting recipes, and requirements. Supports filtering by category.

### [DPS Calculator](tools/DPS%20Calculator/WoV_DPS_Calculator.html)
Calculate and compare damage output across different weapon loadouts. Features:
- Side-by-side loadout comparison
- DPS chart with configurable X/Y axes
- Ammo selection for bows
- Block/Deflect damage reduction modeling
- Preset loadouts & shareable URLs

### [XP Calculator](tools/XP%20Calculator/)
Estimate experience rates and time-to-level for various skills.

### [Formula Reference](formulas/WoV_Formulas.html)
Interactive page documenting game mechanics: damage formulas, XP scaling, and sell price calculations.

---

## 📦 Entity Database

All game item data lives in `data/entities/` as JSON files, loaded at runtime by the Data Browser.

| File | Contents | Count |
|------|----------|-------|
| `weapons.json` | Swords, axes, spears, greatswords, rapiers | Melee weapons |
| `armor.json` | Helmets, platebodies, platelegs, boots, gloves | All armor pieces |
| `shields.json` | Shields & wards | Defensive offhands |
| `jewelry.json` | Rings & amulets | Stat-boosting accessories |
| `gems.json` | Power, magic, and fishing gems | Jewelry attachments |
| `ammo.json` | Arrows (wood, bronze, iron, steel) | Ranged ammunition |
| `weapons.json` | Bows (crude → willow) | Ranged weapons |
| `tools.json` | Pickaxes, fishing rods, smithing hammers, mining gloves | Gathering & crafting tools |
| `ores.json` | Ores & gold dust | Mining resources |
| `bars.json` | Smelted bars (bronze → gold) | Smithing materials |
| `fish.json` | Fish, worm bait | Fishing catches & bait |
| `potions.json` | Brew & bottle recipes | Health, shield, attack, mining, fishing potions |
| `ingredients.json` | Intermediate crafting materials | Essence, vials, flesh, scales, etc. |

### Entity Schema

Each entity typically includes:
```json
{
  "Name": "Item Name",
  "Description": "In-game tooltip description",
  "Icon": "icon_filename",
  "Type": "ITEM_TYPE",
  "Price": 100,
  "Requirements": [{ "Skill": "SKILL_NAME", "Value": 10 }],
  "Stats": [{ "Type": "STAT_TYPE", "Value": 5 }]
}
```

### NPC Data

Monster and boss data lives in `data/npcs/monsters.json`, used by the DPS Calculator for damage-against-enemy modeling.

---

## 🎨 Design

All tools share a consistent dark-themed UI with a medieval fantasy aesthetic. See [`shared/STYLE_REFERENCE.md`](shared/STYLE_REFERENCE.md) for the full design system including colors, typography, and component patterns.

**Key design tokens:**
- Background: `#0a1929` / `#0f2744`
- Accent: `#f6a623` (gold)
- Text: `#e8e0d4` (warm parchment)
- Font: `Cinzel` for headings, `Inter` for body text

---

## 🤝 Contributing

### Adding New Items
1. Add item data to the appropriate JSON file in `data/entities/`
2. Follow the existing schema (Name, Description, Icon, Type, Price, Stats)
3. Place icon sprites (94×95 PNG) in `icons/items/` with matching `Icon` field name

### Updating Formulas
Formula documentation is in `formulas/` as both Markdown (source of truth) and HTML (interactive display).

### Data Sourcing
Item data is sourced directly from in-game screenshots. The `tempPics/` folder (gitignored) is used as a staging area for processing screenshots before extracting data into JSON files.

---

## 📋 Data Completeness

| Category | Name | Description | Icon | Price | Stats |
|----------|:----:|:-----------:|:----:|:-----:|:-----:|
| Weapons | ✅ | ✅ | ✅ | ✅ | ✅ |
| Armor | ✅ | ✅ | ✅ | ✅ | ✅ |
| Shields | ✅ | ✅ | ✅ | ✅ | ✅ |
| Jewelry | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gems | ✅ | ✅ | ✅ | ✅ | ✅ |
| Ammo | ✅ | ✅ | ✅ | ✅ | ✅ |
| Tools | ✅ | ✅ | ✅ | ✅ | ✅ |
| Ores | ✅ | ✅ | ✅ | ✅ | — |
| Bars | ✅ | ✅ | ✅ | ✅ | — |
| Fish | ✅ | ✅ | ✅ | ✅ | — |
| Potions | ✅ | ✅ | ✅ | — | — |
| Ingredients | ✅ | Partial | Partial | Partial | — |

---

## 📄 License

Community project — contributions welcome. Game assets and data belong to the Winds of Valen developers.
