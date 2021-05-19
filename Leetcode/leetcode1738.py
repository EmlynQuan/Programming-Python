# coding=utf-8

def kthLargestValue(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    m = len(matrix)
    n = len(matrix[0])
    dpPrefix = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            dpPrefix[i][j] = dpPrefix[i-1][j] ^ dpPrefix[i][j-1] ^ dpPrefix[i-1][j-1] ^ matrix[i-1][j-1]

    dpPrefix = sum(dpPrefix, [])
    dpPrefix.sort()
    print dpPrefix
    return dpPrefix[-k]


if __name__ == "__main__":
    matrix = [[8,10,5,8,5,7,6,0,1,4,10,6,4,3,6,8,7,9,4,2]]
    kthLargestValue(matrix, 2)