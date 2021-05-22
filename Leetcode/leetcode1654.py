# coding=utf-8

def minimumJumps(forbidden, a, b, x):
    """
    :type forbidden: List[int]
    :type a: int
    :type b: int
    :type x: int
    :rtype: int
    """

    return False


def dfs(forbidden, a, b, x, curPos):
    if curPos > x + b:
        