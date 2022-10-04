# CPE 202 Lab 1a
from typing import Optional, List, Any
from typing import List


# Maybe_List (Optional[List]) is either
# Python List
# or
# None

# Maybe_integer (Optional[int]) is either
# integer
# or
# None

# Maybe_List -> Maybe_integer
def max_list_iter(int_list: Optional[List]) -> Optional[int]:
    """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    elif len(int_list) == 0:
        return None
    elif not all(isinstance(i, int) for i in int_list):
        raise ValueError
    else:
        max = int_list[0]
        for i in int_list:
            if i > max:
                max = i
        return max


# Maybe_List -> Maybe_List
def reverse_list(int_list: Optional[List]) -> Optional[List]:
    """reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError

    new_list: List = []
    for i in int_list:
        new_list = [i] + new_list
    return new_list


# Maybe_List -> None
def reverse_list_mutate(int_list: Optional[List]) -> None:
    """reverses a list of numbers, modifying the input list, returns None
   If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError

    rev_list: List = []
    for i in int_list:
        rev_list = [i] + rev_list
    for i in range(len(rev_list)):
        int_list[i] = rev_list[i]


