# coding=utf-8

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    ret = []
    dfs(ret, n, n, [])
    return ret


def dfs(ret, left, right, curList):
    if left < 0 or right < 0:
        return
    if left == 0 and right == 0:
        ret.append(''.join(curList))
        return
    elif left > right:
        return
    elif left == right:
        curList.append("(")
        dfs(ret, left - 1, right, curList)
    else:
        # 左
        curList.append("(")
        dfs(ret, left - 1, right, curList)

        # 回溯
        curList.pop(-1)

        # 右
        curList.append(")")
        dfs(ret, left, right - 1, curList)

        # 回溯
        curList.pop(-1)

if __name__ == "__main__":
    print generateParenthesis(3)