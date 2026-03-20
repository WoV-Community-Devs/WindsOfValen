# Damage Calculation

> [!CAUTION]
> **We do not currently know how damage reduction works.** The exact mechanics of how enemy Block Power and Deflect Power reduce incoming damage have not been validated against the game's source code. The 75% reduction value used in the DPS calculator is an assumption and may not be accurate.

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

flatDamageBonus = meleePower × EQUIPMENT_POWER_STRENGTH × attackSpeed

maxHit = floor(BASE_DAMAGE + (effectiveAttackLevel × EFFECTIVE_LEVEL_DAMAGE_MULTIPLIER × (weaponDamageBonus + flatDamageBonus)) / DAMAGE_DIVIDER)
```

**Where:**
- `attackLevel` — Attack Level (melee) or Ranged Level (bows), 1–99
- `weaponDamage` — Sum of Quick Damage + Heavy Damage from the weapon
- `attackSpeed` — Speed value on the weapon (1.0–5.0)
- `meleePower` — Total Melee Power or Range Power from all equipped gear (each item's power is individually boosted by its socketed gem, if any)

## Damage Range

```
minHit = floor(maxHit × 0.5)
avgHit = floor(maxHit × 0.75)
maxHit = maxHit
```

Every hit rolls uniformly between `minHit` and `maxHit`.

## Gem Power Bonus

Gems can be socketed into **Ring** and **Amulet** slots. Each gem adds a percentage bonus **only to the Melee/Range Power of the item it is slotted into**, not to total power across all gear.

```
itemPower = floor(baseItemPower × (1 + gemPct / 100))
```

| Gem | Bonus |
|---|---|
| Weak Power Gem | +20% |
| Power Gem | +30% |
| Strong Power Gem | +40% |

## Weapon Types

- **Slash weapons** use Slash Accuracy vs enemy Slash Defence
- **Pierce weapons** (including bows) use Pierce Accuracy vs enemy Pierce Defence
- **Bows** use Ranged Level instead of Attack Level for both accuracy and damage
- **Two-handed weapons** (greatswords, axes, bows) disable the shield slot
