# coding=utf-8


# 动态规划
def minCost1(houses, cost, m, n, target):
    """
    :type houses: List[int]
    :type cost: List[List[int]]
    :type m: int
    :type n: int
    :type target: int
    :rtype: int
    """
    # 便于后面继续比较 将着色统一减一
    houses = [t-1 for t in houses]
    # 动态规划数组
    dp = [[[float("inf") for _ in range(target)] for _ in range(n)] for _ in range(m)]

    # 第一个房子的上色情况
    # 未上色
    if houses[0] == -1:
        # 上色的花费就是cost对应颜色的值
        for j in range(n):
            dp[0][j][0] = cost[0][j]
    # 已经有颜色
    else:
        dp[0][houses[0]][0] = 0

    # 遍历房子
    for i in range(1, m):
        for j in range(n):
            # 当前房子尚未着色 并且给它上色为前一个房子的颜色
            if houses[i] == -1 and houses[i-1] == j:
                for t in range(target):
                    dp[i][j][t] = dp[i-1][j][t] + cost[i][j]
            # 当前房子尚未着色 并且上色为不同的颜色
            if houses[i] == -1 and houses[i-1] != j:
                for t in range(1, target):
                    # 找到当前街区值的对应的最小花费值
                    tempMin = float("inf")
                    for color in range(n):
                        if color != houses[i-1]:
                            tempMin = min(tempMin, dp[i-1][color][t-1])
                    if tempMin != float("inf"):
                        dp[i][j][t] = tempMin + cost[i][j]

            # 当前房子已经着色 并且是当前颜色（不是当前颜色 不需要修改 因为初始化是已经赋值为无穷大）
            elif houses[i] == j:
                # 可以和前一个房子可以连成同一个街区
                if houses[i-1] == j:
                    for t in range(target):
                        dp[i][j][t] = dp[i-1][j][t]
                # 和前一个房子不是同一个街区
                else:
                    for t in range(1, target):
                        tempMin = float("inf")
                        for color in range(n):
                            if color != houses[i - 1]:
                                tempMin = min(tempMin, dp[i - 1][color][t - 1])
                        if tempMin != float("inf"):
                            dp[i][j][t] = tempMin

    ret = float("inf")
    for j in range(n):
        ret = min(ret, dp[m-1][j][target-1])

    if ret == float("inf"):
        return -1
    else:
        return ret

def minCost(houses, cost, m, n, target):
    """
    :type houses: List[int]
    :type cost: List[List[int]]
    :type m: int
    :type n: int
    :type target: int
    :rtype: int
    """
    # 便于后面继续比较 将着色统一减一
    houses = [t-1 for t in houses]
    # 动态规划数组
    dp = [[[float("inf") for _ in range(target)] for _ in range(n)] for _ in range(m)]

    # 遍历房子
    for i in range(m):
        for j in range(n):
            # 如果当前房子已上色且不是当前遍历的颜色
            if houses[i] != -1 and houses[i] != j:
                continue
            # 对街区遍历
            for k in range(target):
                for color in range(n):
                    if j == color:
                        if i == 0:
                            if k == 0:
                                dp[i][j][k] = 0
                        else:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
                    # 当前房子的颜色和前一个颜色不同
                    elif i > 0 and k > 0:
                        dp[i][j][k] = min(dp[i][j][k], dp[i - 1][color][k - 1])
                # 如果可以上色
                if dp[i][j][k] != float("inf") and houses[i] == -1:
                    dp[i][j][k] += cost[i][j]

    ret = float("inf")
    for j in range(n):
        ret = min(ret, dp[m-1][j][target-1])

    if ret == float("inf"):
        return -1
    else:
        return ret



if __name__ == "__main__":
    print minCost(houses=[0, 2, 1, 2, 0], cost=[[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],
            m=5, n=2, target=3)