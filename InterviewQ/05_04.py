# coding=utf-8

def findClosedNumbers(num):
    """
    :type num: int
    :rtype: List[int]
    """
    upper,lower = num, num
    memo = []
    while upper > 0:
        memo.append(upper % 2)
        upper = upper >> 1
    # 从低位开始遍历
    for i in range(len(memo)):


    return [upper, lower]