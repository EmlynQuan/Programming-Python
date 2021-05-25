# coding=utf-8

def reverseParentheses(s):
    """
    :type s: str
    :rtype: str
    """
    length = len(s.replace("(","").replace(")",""))
    ret = [0 for _ in range(length)]
    posL, posR = 0, length-1

    left, right = 0, len(s)-1
    flag = False
    while left < right:
        # 尚未开始括号 不需要翻转的
        if flag == False:
            while s[left] != "(":
                ret[posL] = s[left]
                left += 1
                posL += 1
            while s[left] == "(":
                left += 1
            while s[right] != ")":
                ret[posR] = s[right]
                right -= 1
                posR -= 1
            while s[right] == ")":
                right -= 1
            flag = True
        # 已经开始需要翻转了
        else:
            while s[left] != "(":
                ret[posR] = s[left]
                left += 1
                posR -= 1
            while s[left] == "(":
                left += 1
            while s[right] != ")":
                ret[posL] = s[right]
                right -= 1
                posL += 1
            while s[right] == ")":
                right -= 1

    return "".join(ret)