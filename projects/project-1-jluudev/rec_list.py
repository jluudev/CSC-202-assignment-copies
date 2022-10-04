from __future__ import annotations
from typing import Optional, Any, Tuple


# NodeList is
# None or
# Node(value, rest), where rest is the rest of the NodeList
class Node:
    def __init__(self, value: Any, rest: Optional[Node]):
        self.value = value
        self.rest = rest

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return (self.value == other.value
                    and self.rest == other.rest
                    )
        else:
            return False

    def __repr__(self) -> str:
        return ("Node({!r}, {!r})".format(self.value, self.rest))


# a StrList is one of
# - None, or
# - Node(string, StrList)

# StrList -> string
# Returns first (as determined by Python compare) string in StrList
# If StrList is empty (None), return None
# Must be implemented recursively
def first_string(strlist: Optional[Node]) -> Optional[str]:
    if strlist is None:
        return None
    elif strlist.rest is None:
        return strlist.value
    else:
        if strlist.value < first_string(strlist.rest):
            return strlist.value
        else:
            return first_string(strlist.rest)


# StrList -> (StrList, StrList, StrList)
# Returns a tuple with 3 new StrLists,
# the first one with strings from the input list that start with a vowel,
# the second with strings from the input list that start with a consonant,
# the third with strings that don't start with an alpha character
# Must be implemented recursively
def split_list(strlist: Optional[Node]) -> Tuple[Optional[Node], Optional[Node], Optional[Node]]:
    if strlist is None:
        return (None, None, None)
    else:
        n_list = split_list(strlist.rest)
        vowels_consonants = ['a', 'e', 'i', 'o', 'u', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
                             'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        if strlist.value[0].lower() in vowels_consonants[0:5]:
            return (Node(strlist.value, n_list[0]), n_list[1], n_list[2])
        elif strlist.value[0].lower() in vowels_consonants[5:len(vowels_consonants)]:
            return (n_list[0], Node(strlist.value, n_list[1]), n_list[2])
        else:
            return (n_list[0], n_list[1], Node(strlist.value, n_list[2]))
