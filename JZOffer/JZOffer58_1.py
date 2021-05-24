# coding=utf-8

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    arr = s.split(" ")
    i = 0
    while i < len(arr):
        if arr[i] == "":
            arr.pop(i)
        else:
            i += 1

    left, right = 0, len(arr)-1
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    return " ".join(arr)