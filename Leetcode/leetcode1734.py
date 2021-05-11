# coding=utf-8

def decode(encoded):
    # 首先求第一个元素
    total, odd = 0, 0
    n = len(encoded)
    for i in range(1, n+2):
        total ^= i

    for i in range(1, n, 2):
        odd ^= encoded[i]

    ret = []
    ret.append(total^odd)

    for i in range(n):
        ret.append(ret[-1]^encoded[i])

    return ret
