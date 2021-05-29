# coding=utf-8

def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    # counter = 0
    # for i in range(33):
    #     if (n >> i) & 1 == 1:
    #         counter += 1
    # return counter

    counter = 0
    while n:
        if n & 1:
            counter += 1
        n >>= 1
    return counter
