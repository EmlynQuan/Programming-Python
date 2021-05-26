# coding=utf-8

def reverseParentheses(s):
    """
    :type s: str
    :rtype: str
    """
    myStack = []
    pos = 0
    while pos < len(s):
        # 不是右括号就入栈
        if s[pos] != ")":
            myStack.append(s[pos])
            pos += 1
        # 遇到右括号就出栈
        elif s[pos] == ")":
            temp = []
            while myStack and myStack[-1] != "(":
                temp.append(myStack.pop(-1))
            myStack.pop()
            myStack += temp
            pos += 1

    return "".join(myStack)


if __name__ == "__main__":
    s = "(ed(et(oc))el)"
    print reverseParentheses(s)
