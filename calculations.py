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
    "cumulative_xp": cumulative_xp,
    "xp_between": xp_between,
    "kills_needed": kills_needed,
    "actions_needed": actions_needed,
    # Rates & Duration
    "xp_per_hour": xp_per_hour,
    "time_to_level": time_to_level,
    # Gold & Trading
    "total_cost": total_cost,
    "profit": profit,
}
