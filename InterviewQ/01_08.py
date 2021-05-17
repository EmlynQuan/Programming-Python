# coding=utf-8


def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    m = len(matrix[0])
    ansI = []
    ansJ = []
    # 遍历
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                if i not in ansI:
                    ansI.append(i)
                if j not in ansJ:
                    ansJ.append(j)
    # 行置为0
    for i in ansI:
        for j in range(m):
            matrix[i][j] = 0

    # 列置为0
    for i in ansJ:
        for j in range(n):
            matrix[j][i] = 0

    return matrix



if __name__ == "__main__":

    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print setZeroes(matrix)

