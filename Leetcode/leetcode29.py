# coding=utf-8

def divide(dividend, divisor):
    if dividend == 0:
        return 0

    INT_MIN = 2**31
    INT_MAX = 2**31 - 1

    flag = 1
    if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
        flag = -1

    dividend = dividend if dividend > 0 else -dividend
    divisor = divisor if divisor > 0 else -divisor

    if divisor == 1:
        if dividend > INT_MAX:
            if flag == -1 and dividend <= INT_MIN:
                return -dividend
            else:
                return INT_MAX
        else:
            return flag*dividend

    counter = div(dividend, divisor)

    if counter > INT_MIN:
        return INT_MAX
    elif flag == -1:
        return -counter
    elif counter > INT_MAX:
        return INT_MAX
    else:
        return counter

def div(a, b):
    if a < b:
        return 0
    count = 1
    varb = b
    while varb+varb <= a:
        count += count
        varb += varb

    return count + div(a-varb, b)

