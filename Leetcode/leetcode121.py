# coding=utf-8

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    minprice = float('inf')
    maxprofit = float('-inf')

    for i in range(len(prices)):
        if prices[i] < minprice:
            minprice = prices[i]
        elif maxprofit < prices[i] - minprice:
            maxprofit = prices[i] - minprice

    if maxprofit == float('-inf'):
        return 0
    else:
        return maxprofit