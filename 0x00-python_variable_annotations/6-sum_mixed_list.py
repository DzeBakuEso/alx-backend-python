#!/usr/bin/env python3
"""
This module defines a function sum_mixed_list that sums the elements of a list 
containing both integers and floats.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing both integers and floats.
    
    Args:
        mxd_lst (List[Union[int, float]]): List of integers and floats.

    Returns:
        float: The sum of all the numbers in the list.
    """
    return sum(mxd_lst)
