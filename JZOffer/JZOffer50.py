# coding=utf-8
import collections
def firstUniqChar(s):
    """
    :type s: str
    :rtype: str
    """
    if s == "":
        return " "
    A, B = [], []
    ans = s[0]
    for ch in s:
        if ch in A:
            A.remove(ch)
            B.append(ch)
            if A:
                ans = A[0]
            else:
                ans = " "
        elif ch not in B:
            A.append(ch)
            ans = A[0]
    return ans

