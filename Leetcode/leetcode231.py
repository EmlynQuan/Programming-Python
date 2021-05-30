# coding=utf-8

def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    # if n == 0:
    #     return False
    # while n:
    #     if n == 1:
    #         return True
    #     if n % 2 != 0:
    #         return False
    #     n >>= 1
    # return True

    return n > 0 and n & (n-1) == 0
