#coding=utf-8

def isValidSudoku(board):
    # 判断行是否有重复数字
    for i in range(9):
        flag = [False for _ in range(9)]
        for j in range(9):
            if board[i][j] == '.':
                continue
            else:
                idx = int(board[i][j])-1
                if flag[idx] == True:
                    return False
                else:
                    flag[idx] = True
    # 判断列是否有重复数字
    for i in range(9):
        flag = [False for _ in range(9)]
        for j in range(9):
            if board[j][i] == '.':
                continue
            else:
                idx = int(board[j][i])-1
                if flag[idx] == True:
                    return False
                else:
                    flag[idx] = True

    # 判断3*3单元格是否有重复数字
    for i in range(9):
        row = i // 3
        col = i % 3
        flag = [False for _ in range(9)]
        for y in range(row*3, row*3+3):
            for x in range(col*3, col*3+3):
                if board[y][x] == '.':
                    continue
                else:
                    idx = int(board[y][x])-1
                    if flag[idx] == True:
                        return False
                    else:
                        flag[idx] = True

    return True

if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print isValidSudoku(board)
