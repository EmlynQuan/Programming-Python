# coding=utf-8

def rotate(matrix):
    n = len(matrix)
    # 水平翻转
    for i in range(n//2):
        for j in range(n):
            temp = matrix[n-1-i][j]
            matrix[n - 1 - i][j] = matrix[i][j]
            matrix[i][j] = temp
    # print matrix
    # 按照对角线翻转
    for i in range(n):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    # print matrix
    return matrix


if __name__ == "__main__":
    matrix =[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate(matrix)