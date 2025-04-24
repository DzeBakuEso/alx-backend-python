#!/usr/bin/env python3
"""Module that defines a function to_kv which
returns a tuple of a string and the square of an int/float as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the string and the square of the value (as float).

    Args:
        k (str): The key.
        v (Union[int, float]): The value, which will be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string `k`,
        and the second element is the square of `v` as a float.
    """
    return (k, float(v ** 2))
