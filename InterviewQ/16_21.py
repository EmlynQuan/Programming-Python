# coding=utf-8

def findSwapValues(array1, array2):
    """
    :type array1: List[int]
    :type array2: List[int]
    :rtype: List[int]
    """
    sum1 = sum(array1)
    sum2 = sum(array2)

    array1.sort()
    array2.sort()

    left, right = 0,0
    n1, n2 = len(array1), len(array2)

    val = sum1 - sum2
    while left < n1 and right < n2:
        if 2*(array1[left] - array2[right]) == val:
            return [array1[left], array2[right]]
        elif 2*(array1[left] - array2[right]) < val:
            left += 1
        else:
            right += 1
    return []


