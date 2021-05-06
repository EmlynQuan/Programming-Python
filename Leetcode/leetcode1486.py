# coding=utf-8

def xorOperation(n, start):
    ret = 0
    for i in range(n):
        ret ^= (start + 2*i)
    return ret