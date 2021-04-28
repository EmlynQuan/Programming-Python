# coding=utf-8
import math

def judgeSquareSum(c):
    '''
    判断一个数是否可以拆成两个整数平方的和
    :param c: 给定的数
    :return: 是否可以分解 True / False
    '''

    temp = math.sqrt(c)
    temp = (int)(math.ceil(temp))

    # arr = [i for i in range(temp+1)]
    left, right = 0, temp

    while left <= right:
        temp = left**2 + right**2
        if temp == c:
            return True
        elif temp > c:
            right -= 1
        else:
            left += 1

    return False

if __name__ == "__main__":
    judgeSquareSum(5)