# coding=utf-8

def countTriplets(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    ans = []
    n = len(arr)
    prefixValue = [0 for i in range(n+1)]
    for i in range(1, n+1):
        prefixValue[i] = prefixValue[i-1] ^ arr[i-1]

    for i in range(n-1):
        for j in range(i+1, n):
            k = j
            while k < n:
                a = prefixValue[j] ^ prefixValue[i]
                b = prefixValue[k+1] ^ prefixValue[j]
                if a == b:
                    ans.append([i, j, k])
                k += 1

    return len(ans)