# coding=utf-8

def decode(encoded, first):
    ret = []

    ret.append(first)
    for i in range(len(encoded)):
        temp = encoded[i] ^ ret[-1]
        ret.append(temp)

    return ret