# coding=utf-8

def coinChange(coins, amount):
    '''
    硬币兑换 coins是可兑换的硬币的面值 amount为待兑换的总面值
    '''
    memo = [0 for _ in range(amount+1)]
    return find(coins, amount, memo)

def find(coins, curAmount, memory):
    '''
    找当前给定值是否能够被兑换
    '''
    # # 正好兑换完成
    # if curAmount == 0:
    #     return 1
    # 如果当前值小于0 则不能兑换
    if curAmount < 0:
        return -1
    # 如果当前值为0 恰好可以兑换 返回0
    elif curAmount == 0:
        return 0
    # 备忘录中存在
    if memory[curAmount] != 0:
        return memory[curAmount]
    # 需要计算
    else:
        minValue = curAmount + 1
        # 遍历硬币
        for coin in coins:
            ans = find(coins, curAmount-coin, memory)
            if ans != -1:
                minValue = minValue if ans > minValue else ans

        # 未找到可行解
        if minValue == curAmount + 1:
            memory[curAmount] = -1
        else:
            memory[curAmount] = minValue + 1
    return memory[curAmount]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print coinChange(coins, amount)