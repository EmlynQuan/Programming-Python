# coding=utf-8

def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1
    elif n < 0:
        return 1 / myPow(x, -n)
    # 奇数
    elif n & 1:
        return x * myPow(x, n-1)
    else:
        return myPow(x*x, n // 2)


