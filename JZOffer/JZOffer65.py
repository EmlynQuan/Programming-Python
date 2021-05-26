# coding=utf-8

def add(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    x = 0xffffffff
    # 得到补码
    a, b = a & x, b & x
    while b != 0:
        a, b = (a ^ b), (a & b) << 1 & x
    return a if a <= 0x7fffffff else ~(a ^ x)

