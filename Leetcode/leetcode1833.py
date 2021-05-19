# coding=utf-8

def maxIceCream(costs, coins):
    """
    :type costs: List[int]
    :type coins: int
    :rtype: int
    """
    n = len(costs)
    # 可以全部购买
    if coins >= sum(costs):
        return n
    # 排序
    costs.sort()
    # 贪心去考虑每个雪糕
    i = 0
    while i < n:
        if coins >= costs[i]:
            coins -= costs[i]
        else:
            break
        i += 1
    return i


