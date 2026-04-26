#!/usr/bin/env python3
"""
Calculation Functions in Python for Winds of Valen
This module is universal and can be referenced by AI or turned into different formats as needed
=============================
For AI: Safe, whitelisted functions for game mechanics calculations.
All functions are imported and registered via _CALC_REGISTRY.

Usage in LLM responses:
  [CALC: cumulative_xp(50)]
  [CALC: xp_between(50, 60)]
  [CALC: kills_needed(50, 60, 120)]
"""

import math


# ============================================================================
# XP & LEVELING
# ============================================================================

def level_at_xp(total_xp: float) -> int:
    """Find what level a given amount of cumulative XP corresponds to.

    Inverse of cumulative_xp(). Returns the highest level whose XP
    requirement is <= total_xp.

    Args:
        total_xp: Cumulative XP earned from level 1

    Returns:
        Current level (1-based)

    Formula: floor(1 + 5 × log2(total_xp ÷ 500 + 1)), verified against cumulative_xp()
    """
    if total_xp <= 0:
        return 1
    level = max(1, int(1 + 5 * math.log2(total_xp / 500 + 1)))
    # Step up if int() truncation in cumulative_xp means we actually reached the next level
    while cumulative_xp(level + 1) <= total_xp:
        level += 1
    return level


def cumulative_xp(level: int) -> int:
    """Calculate cumulative XP required to reach a given level.

    Args:
        level: Target level (1-based)

    Returns:
        Total XP needed from level 1 to reach this level

    Formula: TotalXP = 500 * (2^((Level-1)/5) - 1)
    """
    if level < 1:
        return 0
    return int(500 * (2 ** ((level - 1) / 5) - 1))


def xp_between(from_level: int, to_level: int) -> int:
    """Calculate XP needed to progress between two levels.

    Args:
        from_level: Starting level
        to_level: Target level

    Returns:
        XP difference between the two levels
    """
    if to_level < from_level:
        return 0
    return cumulative_xp(to_level) - cumulative_xp(from_level)


def kills_needed(from_level: int, to_level: int, xp_per_kill: float) -> int:
    """Calculate kills needed to level between two levels.

    Args:
        from_level: Starting level
        to_level: Target level
        xp_per_kill: XP granted per enemy kill

    Returns:
        Number of kills needed to reach target level
    """
    if xp_per_kill <= 0:
        return 0
    xp_gap = xp_between(from_level, to_level)
    return math.ceil(xp_gap / xp_per_kill)


def actions_needed(from_level: int, to_level: int, xp_per_action: float) -> int:
    """Calculate actions (fishing, mining, etc.) needed to level.

    Args:
        from_level: Starting level
        to_level: Target level
        xp_per_action: XP granted per action

    Returns:
        Number of actions needed to reach target level
    """
    if xp_per_action <= 0:
        return 0
    xp_gap = xp_between(from_level, to_level)
    return math.ceil(xp_gap / xp_per_action)


# ============================================================================
# RATES & DURATION
# ============================================================================

def xp_per_hour(xp_per_action: float, seconds_per_action: float) -> int:
    """Calculate XP/hour from action rate.

    Args:
        xp_per_action: XP granted per action
        seconds_per_action: Seconds to complete one action

    Returns:
        XP earned per hour
    """
    if seconds_per_action <= 0:
        return 0
    actions_per_hour = 3600 / seconds_per_action
    return int(actions_per_hour * xp_per_action)


def time_to_level(from_level: int, to_level: int, xp_per_hour_rate: float) -> float:
    """Calculate hours needed to level at a given XP/hr rate.

    Args:
        from_level: Starting level
        to_level: Target level
        xp_per_hour_rate: XP earned per hour

    Returns:
        Hours needed to reach target level
    """
    if xp_per_hour_rate <= 0:
        return 0
    xp_gap = xp_between(from_level, to_level)
    return xp_gap / xp_per_hour_rate


# ============================================================================
# COMBAT XP (level-scaled)
# ============================================================================

def xp_multiplier(enemy_level: int) -> float:
    """XP multiplier for an enemy based on its combat level.

    Args:
        enemy_level: Enemy's combat level (1–200+)

    Returns:
        Multiplier applied to damage dealt to compute XP gained

    Formula:
        Level   1–100: 1.0 + level × 0.01   (1.0× → 2.0×)
        Level 101–200: 2.0 + (level-100) × 0.005  (2.0× → 2.5×)
    """
    if enemy_level < 1:
        raise ValueError("Enemy level must be >= 1")
    if enemy_level <= 100:
        return round(1.0 + enemy_level * 0.01, 4)
    return round(2.0 + (enemy_level - 100) * 0.005, 4)


def xp_per_damage(damage: float, enemy_level: int) -> float:
    """XP gained from a single hit on an enemy.

    Args:
        damage:      Damage dealt in one hit
        enemy_level: Enemy's combat level

    Returns:
        XP gained from that hit
    """
    return round(damage * xp_multiplier(enemy_level), 4)


def xp_to_kill(enemy_hp: float, enemy_level: int) -> float:
    """Total XP for killing an enemy (equivalent to dealing damage equal to its full HP).

    Args:
        enemy_hp:    Enemy's total HP
        enemy_level: Enemy's combat level

    Returns:
        XP rewarded for a full kill
    """
    return round(enemy_hp * xp_multiplier(enemy_level), 4)


def combat_xp_per_hour(enemy_hp: float, enemy_level: int, seconds_per_kill: float) -> int:
    """XP per hour from repeatedly killing one enemy type.

    Args:
        enemy_hp:         Enemy's total HP
        enemy_level:      Enemy's combat level
        seconds_per_kill: Average seconds from pull to loot

    Returns:
        XP earned per hour
    """
    if seconds_per_kill <= 0:
        return 0
    kills_per_hour = 3600 / seconds_per_kill
    return int(xp_to_kill(enemy_hp, enemy_level) * kills_per_hour)


def active_stat_xp_per_kill(enemy_hp: float, enemy_level: int) -> float:
    """XP awarded to the active training stat (Attack, Defence, etc.) for one kill.

    XP is split: 75% to the active training stat, 25% to Hitpoints.

    Args:
        enemy_hp:    Enemy's total HP
        enemy_level: Enemy's combat level

    Returns:
        XP credited to the active stat per kill

    Formula: xp_to_kill(enemy_hp, enemy_level) × 0.75
    """
    return round(xp_to_kill(enemy_hp, enemy_level) * 0.75, 4)


def hitpoints_xp_per_kill(enemy_hp: float, enemy_level: int) -> float:
    """XP awarded to the Hitpoints skill for one kill.

    XP is split: 25% to Hitpoints, 75% to the active training stat.

    Args:
        enemy_hp:    Enemy's total HP
        enemy_level: Enemy's combat level

    Returns:
        XP credited to Hitpoints per kill

    Formula: xp_to_kill(enemy_hp, enemy_level) × 0.25
    """
    return round(xp_to_kill(enemy_hp, enemy_level) * 0.25, 4)


def combat_xp_per_hour_real(enemy_hp: float, enemy_level: int,
                              your_dps: float, idle_time: float,
                              damage_share: float = 1.0) -> int:
    """XP/hr accounting for damage share (group bosses) and idle time between kills.

    Generalises both scenarios:
      - Solo / clustered enemies: damage_share=1.0, idle_time=pathing (1–10s typical).
      - Group bosses (e.g. crowded Warden): damage_share=your fraction of total
        damage (0.01–0.15 typical), idle_time=respawn (15s for bosses).

    Args:
        enemy_hp:      Enemy's total HP (use player-scaled HP for scaling bosses)
        enemy_level:   Enemy's combat level (for xp_multiplier)
        your_dps:      Your sustained damage per second
        idle_time:     Downtime per cycle (respawn for bosses, pathing for clusters)
        damage_share:  Fraction of total damage you personally deal (0.0–1.0).
                       Defaults to 1.0 (solo / full credit).

    Returns:
        XP/hr credited to the active training stat (75% split applied).

    Formula:
        group_dps     = your_dps / damage_share
        active_time   = enemy_hp / group_dps       (= enemy_hp * damage_share / your_dps)
        your_damage   = enemy_hp * damage_share     (your contribution per cycle)
        your_xp_cyc   = your_damage * xp_multiplier(lvl) * 0.75
        cycle_time    = active_time + idle_time
        XP/hr         = your_xp_cyc * 3600 / cycle_time
    """
    if your_dps <= 0 or damage_share <= 0 or enemy_hp <= 0:
        return 0
    active_time = enemy_hp * damage_share / your_dps
    your_damage = enemy_hp * damage_share
    your_xp_cyc = your_damage * xp_multiplier(enemy_level) * 0.75
    cycle_time  = active_time + idle_time
    if cycle_time <= 0:
        return 0
    return int(your_xp_cyc * 3600 / cycle_time)


def combat_xp_per_hour_dps(dps: float, enemy_level: int) -> int:
    """XP per hour based on sustained damage per second against an enemy.

    Useful when DPS is known but kill time is not (e.g. group fights, multi-target).

    Args:
        dps:         Damage per second dealt to the enemy
        enemy_level: Enemy's combat level

    Returns:
        XP earned per hour
    """
    if dps <= 0:
        return 0
    return int(dps * xp_multiplier(enemy_level) * 3600)


# ============================================================================
# DAMAGE
# ============================================================================

def flat_damage_bonus(power: float, attack_speed: float) -> float:
    """Flat damage bonus contributed by power and attack speed.

    Args:
        power:        Player's Power stat
        attack_speed: Weapon attack speed

    Returns:
        Flat bonus added to weapon damage before max hit calculation

    Formula: power × 0.333333 × attack_speed
    """
    return power * 0.333333 * attack_speed


def max_hit(attack_level: int, weapon_damage: int, power: float, attack_speed: float) -> int:
    """Maximum single-hit damage for a given loadout.

    Args:
        attack_level:  Player's Attack level
        weapon_damage: Weapon's base damage stat
        power:         Player's Power stat
        attack_speed:  Weapon attack speed

    Returns:
        Maximum damage that can be dealt in one hit

    Formula: floor(5 + (effective_level × 1.1 × (weapon_dmg + 30 + flat_bonus)) / 50)
    """
    effective_level  = attack_level + 8
    weapon_dmg_bonus = weapon_damage + 30
    flat_bonus       = flat_damage_bonus(power, attack_speed)
    return math.floor(5 + (effective_level * 1.1 * (weapon_dmg_bonus + flat_bonus)) / 50)


def damage_range(attack_level: int, weapon_damage: int, power: float, attack_speed: float) -> dict:
    """Min, average, and max hit for a given loadout.

    Args:
        attack_level:  Player's Attack level
        weapon_damage: Weapon's base damage stat
        power:         Player's Power stat
        attack_speed:  Weapon attack speed

    Returns:
        Dict with keys 'min', 'avg', 'max' (all integers)

    Formula: min = floor(max × 0.5),  avg = floor(max × 0.75)
    """
    mx  = max_hit(attack_level, weapon_damage, power, attack_speed)
    mn  = math.floor(mx * 0.5)
    avg = math.floor(mx * 0.75)
    return {"min": mn, "avg": avg, "max": mx}


def min_hit(attack_level: int, weapon_damage: int, power: float, attack_speed: float) -> int:
    """Minimum damage per hit. Equal to floor(max_hit × 0.5).

    Args:
        attack_level:  Player's Attack level
        weapon_damage: Weapon's base damage stat
        power:         Player's Power stat
        attack_speed:  Weapon attack speed

    Returns:
        Minimum damage per hit
    """
    return damage_range(attack_level, weapon_damage, power, attack_speed)["min"]


def avg_hit(attack_level: int, weapon_damage: int, power: float, attack_speed: float) -> int:
    """Average damage per hit. Equal to floor(max_hit × 0.75).

    Args:
        attack_level:  Player's Attack level
        weapon_damage: Weapon's base damage stat
        power:         Player's Power stat
        attack_speed:  Weapon attack speed

    Returns:
        Average damage per hit
    """
    return damage_range(attack_level, weapon_damage, power, attack_speed)["avg"]


def gem_power(base_item_power: int, gem_bonus_pct: int) -> float:
    """Effective power of an item after a gem is socketed.

    Args:
        base_item_power: Item's base Power value
        gem_bonus_pct:   Gem bonus percentage (20 = Weak, 30 = Power, 40 = Strong)

    Returns:
        Effective power after gem bonus applied (not floored — game keeps decimals)

    Formula: base_item_power × (1 + gem_bonus_pct / 100)
    """
    return base_item_power * (1 + gem_bonus_pct / 100)


# ============================================================================
# ACCURACY
# ============================================================================

def accuracy_roll(attack_level: int, equipped_accuracy: int) -> int:
    """Attacker's accuracy roll used in hit chance calculation.

    Args:
        attack_level:      Player's Attack level
        equipped_accuracy: Total equipped Accuracy stat

    Returns:
        Accuracy roll value

    Formula: (attack_level + 8) × (equipped_accuracy + 32)
    """
    return (attack_level + 8) * (equipped_accuracy + 32)


def defence_roll(defence_level: int, equipped_defence: int) -> int:
    """Defender's defence roll used in hit chance calculation.

    Args:
        defence_level:    Enemy's Defence level
        equipped_defence: Enemy's equipped Defence stat

    Returns:
        Defence roll value

    Formula: (defence_level + 8) × (equipped_defence + 16)
    """
    return (defence_level + 8) * (equipped_defence + 16)


def hit_chance(attack_level: int, equipped_accuracy: int,
               defence_level: int, equipped_defence: int) -> float:
    """Probability of landing a hit against a target.

    Args:
        attack_level:      Player's Attack level
        equipped_accuracy: Player's equipped Accuracy stat
        defence_level:     Enemy's Defence level
        equipped_defence:  Enemy's equipped Defence stat

    Returns:
        Hit probability as a float (0.0 – 1.0)

    Formula:
        acc > def: 1 - (def + 2) / (2 × (acc + 1))
        acc ≤ def: acc / (2 × def + 1)
    """
    acc  = accuracy_roll(attack_level, equipped_accuracy)
    defe = defence_roll(defence_level, equipped_defence)
    if acc > defe:
        return 1 - (defe + 2) / (2 * (acc + 1))
    else:
        return acc / (2 * defe + 1)


# ============================================================================
# DPS & TIME TO KILL
# ============================================================================

def attack_interval(attack_speed: float) -> float:
    """Seconds between attacks for a given weapon speed.

    Args:
        attack_speed: Weapon attack speed stat

    Returns:
        Seconds between each attack

    Formula: attack_speed × 0.6
    """
    return attack_speed * 0.6


def dps(attack_level: int, weapon_damage: int, power: float, attack_speed: float,
        defence_level: int, equipped_defence: int, equipped_accuracy: int) -> float:
    """Damage per second against a specific enemy.

    Args:
        attack_level:      Player's Attack level
        weapon_damage:     Weapon's base damage stat
        power:             Player's Power stat
        attack_speed:      Weapon attack speed
        defence_level:     Enemy's Defence level
        equipped_defence:  Enemy's equipped Defence stat
        equipped_accuracy: Player's equipped Accuracy stat

    Returns:
        Average damage dealt per second

    Formula: (avg_hit × hit_chance) / attack_interval
    """
    avg = damage_range(attack_level, weapon_damage, power, attack_speed)["avg"]
    hc  = hit_chance(attack_level, equipped_accuracy, defence_level, equipped_defence)
    ivl = attack_interval(attack_speed)
    return (avg * hc) / ivl


def time_to_kill(monster_hp: float,
                 attack_level: int, weapon_damage: int, power: float, attack_speed: float,
                 defence_level: int, equipped_defence: int, equipped_accuracy: int) -> float:
    """Seconds to kill one monster with a given loadout.

    Args:
        monster_hp:        Enemy's total HP
        attack_level:      Player's Attack level
        weapon_damage:     Weapon's base damage stat
        power:             Player's Power stat
        attack_speed:      Weapon attack speed
        defence_level:     Enemy's Defence level
        equipped_defence:  Enemy's equipped Defence stat
        equipped_accuracy: Player's equipped Accuracy stat

    Returns:
        Seconds needed to kill one monster
    """
    d = dps(attack_level, weapon_damage, power, attack_speed,
            defence_level, equipped_defence, equipped_accuracy)
    return monster_hp / d


def kills_per_hour(monster_hp: float,
                   attack_level: int, weapon_damage: int, power: float, attack_speed: float,
                   defence_level: int, equipped_defence: int, equipped_accuracy: int,
                   respawn_time: float = 15.0) -> float:
    """Kills achievable per hour accounting for kill time and respawn delay.

    Args:
        monster_hp:        Enemy's total HP
        attack_level:      Player's Attack level
        weapon_damage:     Weapon's base damage stat
        power:             Player's Power stat
        attack_speed:      Weapon attack speed
        defence_level:     Enemy's Defence level
        equipped_defence:  Enemy's equipped Defence stat
        equipped_accuracy: Player's equipped Accuracy stat
        respawn_time:      Seconds between kill and next spawn (default 15)

    Returns:
        Kills per hour

    Formula: 3600 / (time_to_kill + respawn_time)
    """
    ttk = time_to_kill(monster_hp, attack_level, weapon_damage, power, attack_speed,
                       defence_level, equipped_defence, equipped_accuracy)
    return 3600 / (ttk + respawn_time)


# ============================================================================
# DROP CHANCE
# ============================================================================

def attempts_for_drop(drop_chance_percent: float) -> int:
    """Calculate average number of attempts needed to receive a drop.

    Args:
        drop_chance_percent: Drop chance as a percentage (e.g. 0.1 for 0.1%, 1 for 1%)

    Returns:
        Average number of attempts (actions, kills, etc.) needed to receive one drop

    Formula: attempts = 100 / drop_chance_percent
    """
    if drop_chance_percent <= 0:
        return 0
    return math.ceil(100 / drop_chance_percent)


def items_for_drop(drop_chance_percent: float, yield_per_action: float) -> int:
    """Calculate average items consumed to receive a drop from a gathering action.

    Args:
        drop_chance_percent: Drop chance as a percentage (e.g. 0.1 for 0.1%)
        yield_per_action: Items yielded per action (e.g. 3 ore per rock mined)

    Returns:
        Average number of items yielded before receiving one drop

    Formula: items = yield_per_action * (100 / drop_chance_percent)
    """
    if drop_chance_percent <= 0:
        return 0
    return math.ceil(yield_per_action * (100 / drop_chance_percent))


# ============================================================================
# SMITHING
# ============================================================================

def smithing_efficiency(smithing_level: int, smithing_power: int) -> float:
    """Crafting speed multiplier from level and power.

    Args:
        smithing_level: Player's Smithing level
        smithing_power: Total Smithing Power (hammer + gloves + gem)

    Returns:
        Efficiency multiplier (e.g. 1.38 = 38% faster)

    Formula: 1.0 + (smithing_level × 0.01) + (smithing_power × 0.01)
    """
    return 1.0 + (smithing_level * 0.01) + (smithing_power * 0.01)


def smithing_craft_time(base_duration: float, smithing_level: int, smithing_power: int) -> float:
    """Actual seconds to craft one item after applying level and power bonuses.

    Args:
        base_duration:  Base craft time in seconds (from wiki item page)
        smithing_level: Player's Smithing level
        smithing_power: Total Smithing Power (hammer + gloves + gem)

    Returns:
        Actual craft time in seconds

    Formula: base_duration / smithing_efficiency(level, power)
    """
    return base_duration / smithing_efficiency(smithing_level, smithing_power)


def smithing_items_per_trip(bars_per_item: int, inventory_size: int = 28) -> int:
    """Items craftable per inventory load before needing to bank for more bars.

    Args:
        bars_per_item:  Number of bars consumed per crafted item
        inventory_size: Inventory slot capacity (default 28)

    Returns:
        Items per trip (floor division)

    Formula: floor(inventory_size / bars_per_item)
    """
    return math.floor(inventory_size / bars_per_item)


def smithing_xp_per_hour(xp_per_item: float, base_duration: float,
                         smithing_level: int, smithing_power: int,
                         bars_per_item: int,
                         trip_time: float = 8.0, inventory_size: int = 28) -> int:
    """Steady-state Smithing XP per hour including banking trips.

    One cycle = craft a full inventory of items + one bank trip.
    Trip time is paid once per inventory load, not per item.

    Args:
        xp_per_item:    Smithing XP granted per crafted item
        base_duration:  Base craft time in seconds (from wiki)
        smithing_level: Player's Smithing level
        smithing_power: Total Smithing Power (hammer + gloves + gem)
        bars_per_item:  Bars consumed per crafted item
        trip_time:      Seconds to bank and return (default 8)
        inventory_size: Inventory slot capacity (default 28)

    Returns:
        XP per hour (rounded down)

    Formula:
        items_per_trip  = floor(inventory_size / bars_per_item)
        craft_time      = base_duration / efficiency
        cycle_time      = items_per_trip × craft_time + trip_time
        xp_per_cycle    = items_per_trip × xp_per_item
        XP/hr           = (xp_per_cycle / cycle_time) × 3600
    """
    ipt        = smithing_items_per_trip(bars_per_item, inventory_size)
    craft_time = smithing_craft_time(base_duration, smithing_level, smithing_power)
    cycle_time = ipt * craft_time + trip_time
    xp_cycle   = ipt * xp_per_item
    return int((xp_cycle / cycle_time) * 3600)


def smithing_gold_per_hour(sell_price: float, base_duration: float,
                           smithing_level: int, smithing_power: int,
                           bars_per_item: int,
                           trip_time: float = 8.0, inventory_size: int = 28) -> int:
    """Steady-state gold earned per hour from selling smithed items.

    Does not account for bar cost — use smithing_profit_per_item for net profit.

    Args:
        sell_price:     Stall sell price per crafted item (gold)
        base_duration:  Base craft time in seconds (from wiki)
        smithing_level: Player's Smithing level
        smithing_power: Total Smithing Power
        bars_per_item:  Bars consumed per crafted item
        trip_time:      Seconds to bank and return (default 8)
        inventory_size: Inventory slot capacity (default 28)

    Returns:
        Gold earned per hour (rounded down)
    """
    ipt        = smithing_items_per_trip(bars_per_item, inventory_size)
    craft_time = smithing_craft_time(base_duration, smithing_level, smithing_power)
    cycle_time = ipt * craft_time + trip_time
    gold_cycle = ipt * sell_price
    return int((gold_cycle / cycle_time) * 3600)


def smithing_xp_per_bar(xp_per_item: float, bars_per_item: int) -> float:
    """Smithing XP gained per bar consumed — useful for comparing item efficiency.

    Args:
        xp_per_item:  Smithing XP granted per crafted item
        bars_per_item: Bars consumed per crafted item

    Returns:
        XP per bar
    """
    return round(xp_per_item / bars_per_item, 4)


def smithing_gold_per_bar(sell_price: float, bars_per_item: int) -> float:
    """Sell value per bar consumed — useful for comparing item gold efficiency.

    Args:
        sell_price:    Stall sell price per crafted item (gold)
        bars_per_item: Bars consumed per crafted item

    Returns:
        Gold per bar
    """
    return round(sell_price / bars_per_item, 4)


def smithing_leftover_bars(total_bars: int, bars_per_item: int) -> int:
    """Bars remaining after crafting as many items as possible from a batch.

    Args:
        total_bars:    Total bars available
        bars_per_item: Bars consumed per crafted item

    Returns:
        Leftover bars (0 if divides evenly)

    Formula: total_bars % bars_per_item
    """
    return total_bars % bars_per_item


def smithing_total_time_from_bars(total_bars: int, bars_per_item: int, base_duration: float,
                                  smithing_level: int = 0, smithing_power: int = 0,
                                  trip_time: float = 8.0, inventory_size: int = 28) -> float:
    """Total seconds to smith an entire batch of bars including all banking trips.

    Args:
        total_bars:     Total bars available
        bars_per_item:  Bars consumed per crafted item
        base_duration:  Base craft time in seconds (from wiki)
        smithing_level: Player's Smithing level (default 0)
        smithing_power: Total Smithing Power (default 0)
        trip_time:      Seconds to bank and return per trip (default 8)
        inventory_size: Inventory slot capacity (default 28)

    Returns:
        Total seconds for the full batch

    Formula:
        items       = floor(total_bars / bars_per_item)
        trips       = ceil(items / items_per_trip)
        total_time  = items × craft_time + trips × trip_time
    """
    items      = smithing_items_from_bars(total_bars, bars_per_item)
    ipt        = smithing_items_per_trip(bars_per_item, inventory_size)
    craft_time = smithing_craft_time(base_duration, smithing_level, smithing_power)
    trips      = math.ceil(items / ipt)
    return round(items * craft_time + trips * trip_time, 2)


def smithing_items_from_bars(total_bars: int, bars_per_item: int) -> int:
    """How many items can be crafted from a given number of bars.

    Args:
        total_bars:    Total bars available
        bars_per_item: Bars consumed per crafted item

    Returns:
        Number of items craftable (floor division)
    """
    return math.floor(total_bars / bars_per_item)


def smithing_total_xp_from_bars(total_bars: int, xp_per_item: float, bars_per_item: int) -> int:
    """Total Smithing XP from converting a batch of bars into items.

    Args:
        total_bars:    Total bars available
        xp_per_item:  XP granted per crafted item
        bars_per_item: Bars consumed per crafted item

    Returns:
        Total XP earned
    """
    return math.floor(smithing_items_from_bars(total_bars, bars_per_item) * xp_per_item)


def smithing_total_gold_from_bars(total_bars: int, sell_price: float, bars_per_item: int) -> int:
    """Total gold from selling all items crafted from a batch of bars.

    Args:
        total_bars:    Total bars available
        sell_price:    Stall sell price per crafted item (gold)
        bars_per_item: Bars consumed per crafted item

    Returns:
        Total gold earned from selling
    """
    return math.floor(smithing_items_from_bars(total_bars, bars_per_item) * sell_price)


def smithing_time_per_bar(base_duration: float, bars_per_item: int,
                          smithing_level: int = 0, smithing_power: int = 0) -> float:
    """Craft time per bar consumed, after applying level and power bonuses.

    Args:
        base_duration:  Base craft time in seconds (from wiki)
        bars_per_item:  Bars consumed per crafted item
        smithing_level: Player's Smithing level (default 0 for base time)
        smithing_power: Total Smithing Power (default 0 for base time)

    Returns:
        Seconds spent crafting per bar consumed

    Formula: smithing_craft_time(base_duration, level, power) / bars_per_item
    """
    return round(smithing_craft_time(base_duration, smithing_level, smithing_power) / bars_per_item, 4)


def smithing_profit_per_item(sell_price: float, bars_per_item: int, bar_cost: float) -> float:
    """Net gold profit per crafted item after bar cost.

    Args:
        sell_price:    Stall sell price per crafted item (gold)
        bars_per_item: Bars consumed per crafted item
        bar_cost:      Gold cost per bar (stall price or calculated from ores)

    Returns:
        Profit per item (can be negative if bars cost more than item sells for)
    """
    return sell_price - (bars_per_item * bar_cost)


def smithing_gp_per_xp(xp_per_item: float, bars_per_item: int, bar_cost: float) -> float:
    """Gross gold spent per XP gained — bar cost only, ignoring sell value.

    All items of the same tier have equal XP/bar, so this metric is identical
    across items in a tier. Use smithing_net_gp_per_xp() for a meaningful
    per-item comparison that accounts for sell-back value.

    Args:
        xp_per_item:   Smithing XP granted per crafted item
        bars_per_item: Bars consumed per crafted item
        bar_cost:      Gold cost per bar

    Returns:
        Gross gold spent per 1 XP gained (lower = cheaper XP ignoring sell)

    Formula: (bars_per_item × bar_cost) / xp_per_item
    """
    if xp_per_item <= 0:
        return 0.0
    return round((bars_per_item * bar_cost) / xp_per_item, 4)


def smithing_net_gp_per_xp(xp_per_item: float, bars_per_item: int,
                            bar_cost: float, sell_price: float) -> float:
    """Net gold cost per XP gained after selling the crafted item.

    Negative = you earn gold while gaining XP (profitable training).
    Positive = you spend gold to gain XP.
    Zero = break-even training.

    Args:
        xp_per_item:   Smithing XP granted per crafted item
        bars_per_item: Bars consumed per crafted item
        bar_cost:      Gold cost per bar
        sell_price:    Stall sell price per crafted item

    Returns:
        Net gold cost per 1 XP (negative = profit per XP)

    Formula: ((bars_per_item × bar_cost) - sell_price) / xp_per_item
    """
    if xp_per_item <= 0:
        return 0.0
    return round(((bars_per_item * bar_cost) - sell_price) / xp_per_item, 4)


def smithing_profit_per_bar(sell_price: float, bars_per_item: int, bar_cost: float) -> float:
    """Net gold profit per bar consumed, after bar cost.

    Args:
        sell_price:    Stall sell price per crafted item (gold)
        bars_per_item: Bars consumed per crafted item
        bar_cost:      Gold cost per bar

    Returns:
        Profit per bar (can be negative). Equal to smithing_gold_per_bar - bar_cost.

    Formula: (sell_price / bars_per_item) - bar_cost
    """
    return round((sell_price / bars_per_item) - bar_cost, 4)


# ── SMELTING (ore → bar) ──────────────────────────────────────────────────────

def smelting_cost(ore1_qty: int, ore1_price: float,
                  ore2_qty: int = 0, ore2_price: float = 0.0) -> float:
    """Ore cost to smelt one bar.

    Args:
        ore1_qty:   Primary ore quantity per bar (e.g. 1 for Mithril Ore)
        ore1_price: Price per primary ore (gold)
        ore2_qty:   Secondary ore quantity per bar (e.g. 2 Coal for Mithril Bar)
        ore2_price: Price per secondary ore (gold, default 0)

    Returns:
        Total ore cost per bar

    Examples:
        Mithril Bar (1 Mithril Ore + 2 Coal): smelting_cost(1, mithril_price, 2, coal_price)
        Bronze Bar (1 Copper Ore):            smelting_cost(1, copper_price)
        Iron Bar   (2 Iron Ore):              smelting_cost(2, iron_price)
    """
    return (ore1_qty * ore1_price) + (ore2_qty * ore2_price)


def smelting_profit(bar_sell_price: float,
                    ore1_qty: int, ore1_price: float,
                    ore2_qty: int = 0, ore2_price: float = 0.0) -> float:
    """Net profit from smelting one bar (bar sell price minus ore cost).

    Args:
        bar_sell_price: Stall sell price of the finished bar (gold)
        ore1_qty:       Primary ore quantity per bar
        ore1_price:     Price per primary ore (gold)
        ore2_qty:       Secondary ore quantity per bar (default 0)
        ore2_price:     Price per secondary ore (gold, default 0)

    Returns:
        Profit per bar (can be negative)
    """
    return bar_sell_price - smelting_cost(ore1_qty, ore1_price, ore2_qty, ore2_price)


# ============================================================================
# GOLD & TRADING
# ============================================================================

def total_cost(quantity: int, unit_price: int) -> int:
    """Calculate total cost for bulk purchase.

    Args:
        quantity: Number of items
        unit_price: Gold per item

    Returns:
        Total gold needed
    """
    return quantity * unit_price


def profit(selling_price: int, cost: int, tax_percent: float = 0) -> int:
    """Calculate profit after tax.

    Args:
        selling_price: Price item sells for
        cost: Total gold spent acquiring item
        tax_percent: Percentage taken by marketplace (default 0)

    Returns:
        Net profit after tax
    """
    tax = int(selling_price * (tax_percent / 100))
    return selling_price - cost - tax


# ============================================================================
# REGISTRY
# ============================================================================
# All functions are automatically discovered and registered by discordbot.py
# via introspection of this module.

CALC_FUNCTIONS = {
    # XP & Leveling
    "level_at_xp": level_at_xp,
    "cumulative_xp": cumulative_xp,
    "xp_between": xp_between,
    "kills_needed": kills_needed,
    "actions_needed": actions_needed,
    # Rates & Duration
    "xp_per_hour": xp_per_hour,
    "time_to_level": time_to_level,
    # Combat XP (level-scaled)
    "xp_multiplier": xp_multiplier,
    "xp_per_damage": xp_per_damage,
    "xp_to_kill": xp_to_kill,
    "combat_xp_per_hour": combat_xp_per_hour,
    "combat_xp_per_hour_dps": combat_xp_per_hour_dps,
    "combat_xp_per_hour_real": combat_xp_per_hour_real,
    "active_stat_xp_per_kill": active_stat_xp_per_kill,
    "hitpoints_xp_per_kill": hitpoints_xp_per_kill,
    # Damage
    "flat_damage_bonus": flat_damage_bonus,
    "max_hit": max_hit,
    "min_hit": min_hit,
    "avg_hit": avg_hit,
    "damage_range": damage_range,
    "gem_power": gem_power,
    # Accuracy
    "accuracy_roll": accuracy_roll,
    "defence_roll": defence_roll,
    "hit_chance": hit_chance,
    # DPS & Time to Kill
    "attack_interval": attack_interval,
    "dps": dps,
    "time_to_kill": time_to_kill,
    "kills_per_hour": kills_per_hour,
    # Drop Chance
    "attempts_for_drop": attempts_for_drop,
    "items_for_drop": items_for_drop,
    # Smithing
    "smithing_efficiency": smithing_efficiency,
    "smithing_craft_time": smithing_craft_time,
    "smithing_items_per_trip": smithing_items_per_trip,
    "smithing_xp_per_hour": smithing_xp_per_hour,
    "smithing_gold_per_hour": smithing_gold_per_hour,
    "smithing_xp_per_bar": smithing_xp_per_bar,
    "smithing_gold_per_bar": smithing_gold_per_bar,
    "smithing_time_per_bar": smithing_time_per_bar,
    "smithing_gp_per_xp": smithing_gp_per_xp,
    "smithing_net_gp_per_xp": smithing_net_gp_per_xp,
    "smithing_profit_per_bar": smithing_profit_per_bar,
    "smithing_leftover_bars": smithing_leftover_bars,
    "smithing_total_time_from_bars": smithing_total_time_from_bars,
    "smithing_items_from_bars": smithing_items_from_bars,
    "smithing_total_xp_from_bars": smithing_total_xp_from_bars,
    "smithing_total_gold_from_bars": smithing_total_gold_from_bars,
    "smithing_profit_per_item": smithing_profit_per_item,
    "smelting_cost": smelting_cost,
    "smelting_profit": smelting_profit,
    # Gold & Trading
    "total_cost": total_cost,
    "profit": profit,
}
