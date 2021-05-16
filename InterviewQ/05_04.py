# coding=utf-8

def findClosedNumbers(num):
    """
    :type num: int
    :rtype: List[int]
    """
    upper,lower = num, num
    temp = num
    value = []
    for k in range(30, -1, -1):
        value.append(bit = (temp >> 1) & 1)



    return [upper, lower]