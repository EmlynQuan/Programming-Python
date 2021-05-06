# coding=utf-8

def generateMatrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    counter = 0

    # right -> down -> left -> up
    moveJ = [1,0,-1,0]
    moveI = [0,1,0,-1]

    i, j, pos = 0, -1, 0
    while counter < n**2:
        nextI = i + moveI[pos]
        nextJ = j + moveJ[pos]
        # 如果可以取到
        if 0 <= nextI < n and 0 <= nextJ < n and matrix[nextI][nextJ] == 0:
            i, j = nextI, nextJ
            counter += 1
            matrix[i][j] = counter
        else:
            pos = pos + 1
            pos %= 4

    print matrix


if __name__ == "__main__":
    generateMatrix(4)