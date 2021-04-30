# coding=utf-8

def gameOfLife(board):
    n = len(board)
    m = len(board[0])
    flag = []

    # 遍历每个位置
    for i in range(n):
        for j in range(m):
            # print str(i) + ", " + str(j)
            # 四种规则
            # 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
            # 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
            # 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
            # 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
            answer = getNeighbor(board, i, j, n, m)
            if board[i][j] == 1:
                if answer < 2 or answer > 3:
                    flag.append([i, j])
            elif answer == 3:
                flag.append([i, j])

    for pos in flag:
        board[pos[0]][pos[1]] ^= 1

    return

def getNeighbor(board, i, j, n, m):
    oneNum = 0

    moveI = [-1,-1,-1,0,0,1,1,1]
    moveJ = [-1,0,1,-1,1,-1,0,1]

    # 遍历8个位置
    for t in range(8):
        curI = i + moveI[t]
        curJ = j + moveJ[t]
        # 判断是有效位置
        if curI >= 0 and curI < n and curJ >= 0 and curJ < m:
            if board[curI][curJ] == 1:
                oneNum += 1

    return oneNum


if __name__ == "__main__":
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    print gameOfLife(board)