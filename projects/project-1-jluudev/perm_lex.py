from typing import List
# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in: str) -> List:
    '''perm_gen_lex takes a str that is in lexicographic order and returns a list of all permutations of that string
    in lexicographic order. If the string is empty, an empty list is returned.'''
    perm_list = []
    if len(str_in) == 0:
        return []
    elif len(str_in) == 1:
        return [str_in]
    else:
        for i in range(len(str_in)):
            simp_str = ""
            for c in str_in:
                if c != str_in[i]:
                    simp_str += c
            perm = perm_gen_lex(simp_str)
            for j in perm:
                perm_list.append(str_in[i] + j)
    return perm_list

