#coding=utf-8

def isPowerOfFour(n):
    """
    :type n: int
    :rtype: bool
    """
    return n > 0 and n & (n-1) == 0 and n % 3 == 1
    return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0