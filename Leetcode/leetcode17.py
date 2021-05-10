# coding=utf-8


def letterCombinations(digits):
    myDict = {
        '2':['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    if digits == "":
        return []

    ret = myDict[digits[0]]
    n = len(digits)
    for i in range(1,n):
        prefix = [c for c in ret]
        ret = []
        for temp in myDict[digits[i]]:
            for pre in prefix:
                ret.append(pre+temp)

    return ret


