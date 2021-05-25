# coding=utf-8

def replaceSpace(s):
    """
    :type s: str
    :rtype: str
    """
    arr = s.split(" ")
    return "%20".join(arr)
