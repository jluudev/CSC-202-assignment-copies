
# Given integer n, returns True or False based on reachability of goal
# See write up for "rules" for bears
def bears(n: int) -> bool:
    '''bears takes in an integer n, which is the number of bears. The function returns True if n can reach 42
    or else it returns False'''
    if n == 42:
        return True
    elif n < 42 or (not n % 2 == 0 and not n % 3 == 0 and n % 4 == 0 and not n % 5 == 0):
        return False
    if n % 2 == 0: #when divisible by 2, take away n // 2 bears
        if bears(n - (n // 2)):
            return True
    if n % 3 == 0 or n % 4 == 0: #when divisible by 3 or 4, take away the product of the last two digits bears.
        last_dig_1 = n % 10
        last_dig_2 = ((n % 100) - (n % 10)) // 10
        if bears(n - (last_dig_1 * last_dig_2)):
            return True
    if n % 5 == 0: #when n is divisible by 5, take away 42 bears
        if bears(n - 42):
            return True
    return False



