#!/usr/bin/env python3
"""
This module provides a type-annotated function that returns
the floor of a float number.
"""

import math

def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number.

    Args:
        n (float): The floating-point number to floor.

    Returns:
        int: The floor value of the float.
    """
    return math.floor(n)
