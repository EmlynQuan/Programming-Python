# coding=utf-8

def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if len(matrix) == 0:
        return []
    n = len(matrix)
    m = len(matrix[0])
    # 右下左上
    spinX = [1,0,-1,0]
    spinY = [0,1,0,-1]
    x, y, dir = 0, 0, 0
    visited = [[0 for _ in range(m)] for _ in range(n)]
    ret = [matrix[0][0]]
    visited[0][0] = 1
    # 开始循环
    while True:
        nextX = x + spinX[dir]
        nextY = y + spinY[dir]
        # 不是非法位置 且并未访问过
        if 0 <= nextX < m and 0 <= nextY < n and visited[nextY][nextX] == 0:
            x = nextX
            y = nextY
            ret.append(matrix[y][x])
            visited[y][x] = 1
        # 需要变换方向
        elif len(ret) < n*m:
            dir = (dir + 1) % 4
        # 遍历完成
        else:
            return ret

