# coding=utf-8

def romanToInt(s):
    # value = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    # key = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

    myDict = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90,
            'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}

    ret = 0
    n = len(s)
    if n == 0:
        return ret
    elif n == 1:
        return myDict[s[0]]
    else:
        pos = 0
        while pos < n:
            if pos < n-1 and myDict[s[pos]] < myDict[s[pos+1]]:
                ret -= myDict[s[pos]]
            else:
                ret += myDict[s[pos]]
            pos += 1
        return ret