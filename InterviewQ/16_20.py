# coding=utf-8

def getValidT9Words(num, words):
    """
    :type num: str
    :type words: List[str]
    :rtype: List[str]
    """
    myDict = {'2':['a', 'b', 'c'],
              '3':['d', 'e', 'f'],
              '4':['g', 'h', 'i'],
              '5':['j', 'k', 'l'],
              '6':['m', 'n', 'o'],
              '7':['p', 'q', 'r', 's'],
              '8':['t', 'u', 'v'],
              '9':['w', 'x', 'y', 'z']}

    for i in range(len(num)):
        j = 0
        while j < len(words):
            if words[j][i] not in myDict[num[i]]:
                words.pop(j)
            else:
                j += 1

    return words

