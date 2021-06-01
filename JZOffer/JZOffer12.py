# coding=utf-8

def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    n = len(board)
    m = len(board[0])

    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0]:
                visited = [[0 for _ in range(m)] for _ in range(n)]
                visited[i][j] = 1
                if dfs(board, word, 1, visited, i, j):
                    return True
                visited[i][j] = 0
    return False

def dfs(grid, word, pos, visited, i, j):
    n,m = len(grid), len(grid[0])
    if pos >= len(word):
        return True
    else:
        # 上 下 左 右
        iAdd = [-1,1,0,0]
        jAdd = [0,0,-1,1]

        for x in range(4):
            tempI = i+iAdd[x]
            tempJ = j+jAdd[x]
            if 0 <= tempI < n and 0 <= tempJ < m:
                if grid[tempI][tempJ] == word[pos] and visited[tempI][tempJ] == 0:
                    visited[tempI][tempJ] = 1
                    if dfs(grid, word, pos+1, visited, tempI, tempJ):
                        return True
                    # 回溯
                    visited[tempI][tempJ] = 0
        return False


# 可以不用visit数组保存 直接将访问过的位置元素置为别的元素 回溯再恢复即可
