# coding=utf-8

def minSteps(s, t):
    counterS = [0 for _ in range(26)]
    counterT = [0 for _ in range(26)]

    i = 0
    while i < len(s):
        idx = ord(s[i]) - ord('a')
        counterS[idx] += 1
        idx = ord(t[i]) - ord('a')
        counterT[idx] += 1
        i += 1

    print counterS
    print counterT
    pCount = 0
    for i in range(26):
        temp = counterS[i]-counterT[i]
        if temp > 0:
            pCount += temp

    return pCount


if __name__ == "__main__":
    s = "sasdw"
    t = "asasa"
    print minSteps(s, t)