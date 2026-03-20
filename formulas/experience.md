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
