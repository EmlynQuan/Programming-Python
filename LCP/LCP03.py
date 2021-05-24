# coding=utf-8

def robot(command, obstacles, x, y):
    """
    :type command: str
    :type obstacles: List[List[int]]
    :type x: int
    :type y: int
    :rtype: bool
    """
    # 初始位置
    varX, varY, bitNum = 0, 0, 30
    path = {}
    path[varX << bitNum | varY] = 0
    # 遍历指令
    for i in range(len(command)):
        # 向上
        if command[i] == 'U':
            varY += 1
        else:
            varX += 1
        path[varX << bitNum | varY] = 0

    # 判断是否能够在前面的路径中遇到障碍物
    for ox, oy in obstacles:
        if ox <= x and oy <= y:
            minStep = min(ox//varX, oy//varY)
            ox -= minStep * varX
            oy -= minStep * varY
            if ox << bitNum | oy in path.keys():
                return False

    minStep = min(x//varX, y//varY)
    x -= minStep * varX
    y -= minStep * varY
    # 判断是否能够到终点
    if x << bitNum | y not in path.keys():
        return False
    return True


if __name__ == "__main__":
    command = "RRRUUU"
    obstacles = [[3, 0]]
    x = 3
    y = 3
    print robot(command, obstacles, x, y)