# Sell Price Formula

## Overview

When selling items to a shop, the gold received is **70%** of the item's listed Price (the gold value shown on the item tooltip).

## Formula

```
sellPrice = floor(price × 0.7)
```

**Where:**
- `price` — The gold value displayed on the item tooltip (bottom-right corner)
- `sellPrice` — The gold received when selling to a shop

## Reverse Calculation

To estimate an item's Price from a known sell value:

```
estimatedPrice = sellCost / 0.7
```

> [!NOTE]
> Several items in the database have `Price` values estimated from `Smithing.SellCost` using this reverse formula. These estimated prices are consistent with all verified screenshot data but have not been individually confirmed via tooltip screenshots.

## Verified Examples

| Item | Price (tooltip) | Sell Price (70%) |
|---|---|---|
| Bronze Sword | 60g | 42g |
| Iron Sword | 150g | 105g |
| Steel Sword | 300g | 210g |
| Mithril Sword | 1,500g | 1,050g |
| Bronze Platebody | 100g | 70g |
| Iron Platebody | 250g | 175g |
| Steel Platebody | 500g | 350g |
| Mithril Platebody | 2,500g | 1,750g |
| Mithril Helmet | 1,000g | 700g |

All verified pairs show an exact **70%** ratio with no exceptions found.
