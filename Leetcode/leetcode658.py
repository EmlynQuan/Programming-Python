# coding=utf-8
import math

def findClosestElements(arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    # 先从中找到x所处的位置
    idx = 0
    while idx < len(arr):
        if arr[idx] <= x:
            idx += 1
            continue
        else:
            break
    left, right = idx-1, idx
    Lgap = float('inf') if left < 0 else math.abs(x - arr[left])
    Rgap = float('inf') if right >= len(arr) else math.abs(x - arr[right])

    # 找k个
    resultL = []
    resultR = []
    while k > 0:
        if Lgap <= Rgap:
            resultL.append(arr[left])
            left -= 1
            if left >= 0:
                Lgap = math.abs(x-arr[left])
            else:
                Lgap = float('inf')
        else:
            resultR.append(arr[right])
            right += 1
            if right < len(arr):
                Rgap = math.abs(x - arr[right])
            else:
                Rgap = float('inf')
        k -= 1

    result = []
    for i in range(len(resultL)-1, -1, -1):
        result.append(resultL[i])
    result.extend(resultR)

    return result



