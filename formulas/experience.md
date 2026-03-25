# Experience Calculation

## XP Required for a Level

```
RequiredXP = 500 × (2^((Level - 1) / 5) - 1)
```

**Where:**
- `Level` — The target level (1–99)
- `RequiredXP` — Total XP needed to reach that level

**Notes:**
- At Level 1, `RequiredXP = 0` (no XP needed)
- XP requirement doubles every 5 levels
- The base scaling factor is `500`

## Example Values

| Level | Required XP |
|---|---|
| 1 | 0 |
| 5 | ~319 |
| 10 | ~1,828 |
| 20 | ~7,653 |
| 50 | ~255,489 |
| 99 | ~52,428,300 |

## Combat XP Multiplier

The combat XP multiplier is a piecewise function based on the player's combat level:

```
if Level ≤ 100:
    combatXpMultiplier = 1 + (Level × 0.01)
else:
    combatXpMultiplier = 2 + ((Level - 100) × 0.005)
```

**Where:**
- `Level` — The player's current combat level
- For levels 1–100, the multiplier increases by **0.01** per level (ranging from 1.01 at level 1 to 2.0 at level 100)
- Past level 100, the multiplier increases by **0.005** per level (e.g., 2.005 at level 101, 2.01 at level 102, etc.)

### Example Values

| Level | Multiplier |
|---|---|
| 1 | 1.01 |
| 50 | 1.50 |
| 100 | 2.00 |
| 120 | 2.10 |
| 150 | 2.25 |
| 200 | 2.50 |
