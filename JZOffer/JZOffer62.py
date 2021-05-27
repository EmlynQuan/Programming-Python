# coding=utf-8

def lastRemaining(n, m):
    """
    :type n: int
    :type m: int
    :rtype: int
    """
    if n == 1:
        return 0
    else:
        temp = range(n)
        pos, t = 0, 0
        while len(temp) > 1:
            if m > len(temp):
                t = m % len(temp)
            else:
                t = m
            idx = (pos+t) % len(temp)
            temp.pop(idx)
            pos = (idx+1) % len(temp)
        return temp[0]
