# coding=utf-8

def myAtoi(s):
    pos = -1
    negFlag = False
    flag = True
    ret = []
    INT_MAX = 2**31
    while pos+1 < len(s):
        pos += 1
        # 还未读入数字
        if flag:
            if s[pos] == " ":
                continue
            elif ord('0') <= ord(s[pos]) <= ord("9"):
                ret.append(int(s[pos]))
                flag = False
                continue
            elif s[pos] == "-":
                negFlag = True
                flag = False
            elif s[pos] == "+":
                flag = False
            else:
                break
        # 已经开始读数字了
        else:
            # 是数字
            if ord('0') <= ord(s[pos]) <= ord("9"):
                ret.append(int(s[pos]))
            else:
                break

    answer = 0
    for i in range(len(ret)):
        j = len(ret) - i - 1
        answer += 10**i * ret[j]

    # 是负数
    if negFlag:
        if answer > INT_MAX:
            return -1*INT_MAX
        else:
            return -1*answer
    else:
        if answer > INT_MAX-1:
            return INT_MAX-1
        else:
            return answer