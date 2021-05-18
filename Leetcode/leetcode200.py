# coding=utf-8

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    counter = 0
    addI = [-1, 1, 0, 0]
    addJ = [0, 0, -1, 1]
    # 遍历每个点
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and visited[i][j] == 0:
                queue = [[i,j]]
                visited[i][j] = 1
                dfs(grid, visited, queue, m, n, addI, addJ)
                counter += 1
    return counter

# 深度优先搜索岛屿
def dfs(grid, visited, queue, m, n, I, J):
    if not queue:
        return
    else:
        temp = queue[-1]
        for i in range(4):
            x = temp[0] + I[i]
            y = temp[1] + J[i]
            if 0 <= x < m and 0 <= y < n and visited[x][y] == 0 and grid[x][y] == '1':
                visited[x][y] = 1
                queue.append([x, y])
                dfs(grid, visited, queue, m, n, I, J)
                queue.pop()


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print numIslands(grid)