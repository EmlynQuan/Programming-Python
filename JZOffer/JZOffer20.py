# coding=utf-8

def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    if isDecimal(s):
        return True
    if isInteger(s):
        return True
    for i in range(len(s)):
        if s[i] == 'e' or s[i] == 'E':
            if isInteger(s[:i], right=False) or isDecimal(s[:i], right=False):
                if isInteger(s[i+1:], left=False):
                    return True
                else:
                    break
            else:
                break
    return False

def isDecimal(s, left=True, right=True):
    '''
    判断是小数
    :param self:
    :param s:
    :return:
    '''
    if left:
        l = 0
        while l < len(s):
            if s[l] == " ":
                l += 1
            else:
                break
        s = s[l:]
    if right:
        r = len(s)-1
        while r >= 0:
            if s[r] == " ":
                r -= 1
            else:
                break
        s = s[:r+1]

    flag = False
    counter = 0
    # 遍历每个字符
    for i in range(len(s)):
        if s[i] == '+' or s[i] == '-':
            if i == 0:
                continue
            else:
                return False
        elif s[i] == ".":
            if counter == 0:
                counter += 1
                continue
            else:
                return False
        elif ord('0') <= ord(s[i]) <= ord('9'):
            flag = True
            continue
        else:
            return False
    return flag



def isInteger(s, left=True, right=True):
    '''
    判断是整数
    :param self:
    :param s:
    :return:
    '''
    if left:
        l = 0
        while l < len(s):
            if s[l] == " ":
                l += 1
            else:
                break
        s = s[l:]
    if right:
        r = len(s) - 1
        while r >= 0:
            if s[r] == " ":
                r -= 1
            else:
                break
        s = s[:r + 1]

    flag = False
    # 遍历每个字符
    for i in range(len(s)):
        if s[i] == '+' or s[i] == '-':
            if i == 0:
                continue
            else:
                return False
        elif ord('0') <= ord(s[i]) <= ord('9'):
            flag = True
            continue
        else:
            return False
    return flag


if __name__ == "__main__":
    s = "  .1"
    print isNumber(s)