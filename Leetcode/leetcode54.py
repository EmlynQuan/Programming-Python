# coding=utf-8

def spiralOrder(matrix):
    '''
    给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
    '''
    n = len(matrix)
    m = len(matrix[0])
    # 结果
    answer = []
    action = 0
    # 动作 右-> 下-> 左-> 上
    moveI = [0, 1, 0, -1]
    moveJ = [1, 0, -1, 0]

    posI = 0
    posJ = 0
    flag = [[0 for _ in range(m)] for _ in range(n)]

    answer.append(matrix[posI][posJ])
    flag[posI][posJ] = 1

    # 顺时针旋转
    while True:
        if len(answer) == n*m:
            return answer

        nextI = posI+moveI[action]
        nextJ = posJ+moveJ[action]
        # 可以继续
        if nextI >= 0 and nextI < n and nextJ >= 0 and nextJ < m and flag[nextI][nextJ] == 0:
            posI = nextI
            posJ = nextJ
            answer.append(matrix[posI][posJ])
            flag[posI][posJ] = 1
        # 换方向
        else:
            action += 1
            action %= 4

    return answer


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print spiralOrder(matrix)