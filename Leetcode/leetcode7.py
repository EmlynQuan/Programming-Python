# coding=utf-8

def reverse(self, x):
    INT_MIN, INT_MAX = -2**31, 2**31-1
    ans = 0
    flag = False
    if x < 0:
        flag = True
        x = -1*x
    while True:
        temp = x % 10
        ans = ans * 10 + temp
        if ans < INT_MIN or ans > INT_MAX:
            return 0
        if x < 10:
            break
        x //= 10
    if flag:
        ans = -1*ans
    return ans

