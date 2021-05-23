# coding=utf-8

def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    jewelDict = {}
    for i in range(len(jewels)):
        jewelDict[jewels[i]] = 1

    ret = 0
    for i in range(len(stones)):
        if stones[i] in jewelDict.keys():
            ret += 1

    return ret


