#!/usr/bin/env python3
"""Module with a function that takes an iterable of sequences and returns a list of tuples with each element and its length."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Computes the length of each element in an iterable sequence.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence-type elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each with the original element and its length.
    """
    return [(i, len(i)) for i in lst]
