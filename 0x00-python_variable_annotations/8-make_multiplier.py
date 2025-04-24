#!/usr/bin/env python3
"""Module that defines a function make_multiplier which
returns a function that multiplies a float by a given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a multiplier function.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the product of it and `multiplier`.
    """
    return lambda x: x * multiplier
