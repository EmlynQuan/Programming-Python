# coding=utf-8

def reverseLeftWords(s, n):
    """
    :type s: str
    :type n: int
    :rtype: str
    """
    length = len(s)
    arr = [0 for _ in range(length)]
    for i in range(length):
        if i < n:
            arr[length-n+i] = s[i]
        else:
            arr[i-n] = s[i]
    return "".join(arr)


