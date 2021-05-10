# coding=utf-8

def decode(encoded):

    n = len(encoded) + 1
    for i in range(1, n+1):
        prem = [i]
        for j in range(n-1):
            temp = encoded[j] ^ prem[-1]
            if temp in prem or temp <= 0 or temp > n:
                break
            else:
                prem.append(temp)

        if len(prem) == n:
            return prem