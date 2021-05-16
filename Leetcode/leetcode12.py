# coding=utf-8

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    value = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    key = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    ret = []
    for i in range(len(key) - 1, -1, -1):
        temp = num // key[i]
        while temp > 0:
            ret.append(value[i])
            temp -= 1
        num = num % key[i]

    return ''.join(ret)


if __name__ == "__main__":
    print intToRoman(1994)
