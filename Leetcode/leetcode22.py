# coding=utf-8

def generateParenthesis(n):
    '''
    给定括号对数 返回所有可能的字符串（列表格式）
    '''
    ret = []
    # 左右括号的可用个数 left, right = n, n
    dfs(n, n, [], ret)
    return ret

def dfs(left, right, answer, arr):
    # 到结束
    if left == 0 and right == 0:
        arr.append("".join(answer))
        # print arr
        return arr
    # 如果剩余左括号大于等于右括号 就必须放左括号
    elif left >= right:
        answer.append('(')
        dfs(left - 1, right, answer, arr)
        answer.pop(-1)
    # 剩余左括号小于右括号数量 只要数量大于0 放左、右均可
    else:
        if left > 0:
            # 放左括号
            answer.append('(')
            dfs(left-1, right, answer, arr)
            answer.pop(-1)
        if right > 0:
            # 放右括号
            answer.append(')')
            dfs(left, right-1, answer, arr)
            answer.pop(-1)

if __name__ == "__main__":
    print generateParenthesis(3)