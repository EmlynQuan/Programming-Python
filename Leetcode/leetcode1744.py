# coding=utf-8

def canEat(candiesCount, queries):
    """
    :type candiesCount: List[int]
    :type queries: List[List[int]]
    :rtype: List[bool]
    """
    n = len(candiesCount)
    # dp[i]存储下标类i之前的糖
    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + candiesCount[i - 1]

    ans = []
    for idx, [type, day, cap] in enumerate(queries):
        # 是从第0天开始吃糖
        # 在最喜欢天之前就会吃完糖
        if day >= dp[type + 1]:
            ans.append(False)
        # 在最喜欢天之后都吃不完前面的糖
        elif (day + 1) * cap <= dp[type]:
            ans.append(False)
        else:
            ans.append(True)
    return ans


if __name__ == "__main__":
    candiesCount = [5, 2, 6, 4, 1]
    queries = [[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]]
    canEat(candiesCount, queries)


