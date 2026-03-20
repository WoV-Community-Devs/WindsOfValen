# Damage Calculation

> [!CAUTION]
> **We do not currently know how damage reduction works.** The exact mechanics of how enemy `BLOCK_POWER` and `DEFLECT_POWER` reduce incoming damage have not been validated against the game's source code. The 75% reduction value used in the DPS calculator is an assumption and may not be accurate.

## Constants

| Constant | Value |
|---|---|
| `BASE_DAMAGE` | 5 |
| `BASE_EFFECTIVE_LEVEL` | 8 |
| `EFFECTIVE_LEVEL_DAMAGE_MULTIPLIER` | 1.1 |
| `BASE_EQUIPMENT_DAMAGE` | 30 |
| `EQUIPMENT_POWER_STRENGTH` | 0.333333 |
| `DAMAGE_DIVIDER` | 50 |

## Max Hit

```
effectiveAttackLevel = attackLevel + BASE_EFFECTIVE_LEVEL

weaponDamageBonus = weaponDamage + BASE_EQUIPMENT_DAMAGE

flatDamageBonus = power × EQUIPMENT_POWER_STRENGTH × ATTACK_SPEED

maxHit = floor(BASE_DAMAGE + (effectiveAttackLevel × EFFECTIVE_LEVEL_DAMAGE_MULTIPLIER × (weaponDamageBonus + flatDamageBonus)) / DAMAGE_DIVIDER)
```

**Where:**
- `attackLevel` — `ATTACK` level (melee) or `RANGED` level (bows), 1–99
- `weaponDamage` — Sum of `QUICK_DAMAGE` + `HEAVY_DAMAGE` from the weapon
- `ATTACK_SPEED` — Speed stat on the weapon (1.0–5.0)
- `power` — Total `MELEE_POWER` or `RANGE_POWER` from all equipped gear (each item's power is individually boosted by its socketed gem, if any)

## Damage Range

```
minHit = floor(maxHit × 0.5)
avgHit = floor(maxHit × 0.75)
maxHit = maxHit
```

Every hit rolls uniformly between `minHit` and `maxHit`.

## Gem Power Bonus

Gems can be socketed into `RING` and `AMULET` slots. Each gem has a `StatType` (e.g., `MELEE_POWER`) and a `ValueType` of `PERCENTAGE`. The gem bonus applies **only to the matching stat on the item it is slotted into** — a gem with `StatType: MELEE_POWER` will not affect `RANGE_POWER`, and vice versa.

```
itemPower = floor(baseItemPower × (1 + Value / 100))
```

| Gem | StatType | Value |
|---|---|---|
| Weak Power Gem | `MELEE_POWER` | +20% |
| Power Gem | `MELEE_POWER` | +30% |
| Strong Power Gem | `MELEE_POWER` | +40% |

## Weapon Types

- **Slash weapons** — Use `SLASH_ACCURACY` vs enemy `SLASH_DEFENSE`
- **Pierce weapons** (including bows) — Use `PIECE_ACCURACY` vs enemy `PIECE_DEFENSE`
- **Bows** (`BOW`) — Use `RANGED` level instead of `ATTACK` level for both accuracy and damage
- **Two-handed weapons** (`WEAPON_2H`, `BOW`) — Disable the `SHIELD` slot
