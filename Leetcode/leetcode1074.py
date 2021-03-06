# coding=utf-8

def numSubmatrixSumTarget(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: int
    """
    n, m,counter = len(matrix), len(matrix[0]), 0
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    # dp[i+1][j+1] 存储的是从[0,0]到[i,j]这个网格的元素和
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i-1][j-1]

    for start_i in range(1, n+1):
        for end_i in range(start_i, n+1):
            myDict = {}
            for j in range(1, m+1):
                val = dp[end_i][j]-dp[start_i-1][j]
                if val == target:
                    counter += 1
                if val-target in myDict.keys():
                    counter += myDict[val-target]
                myDict[val] = myDict.get(val, 0) + 1

    return counter

if __name__ == "__main__":
    matrix = [[0,1,0],[1,1,1],[0,1,0]]
    print numSubmatrixSumTarget(matrix, 0)