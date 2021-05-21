# coding=utf-8

def maxUncrossedLines_dfs(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: int
    """
    # candidate 存储候选线的索引
    candidate = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                candidate.append([i, j])

    lines = []
    if len(candidate) <= 1:
        return len(candidate)
    else:
        return dfs(candidate, lines, 0)


def dfs(candidate, lines, idx):
    # 候选线遍历结束
    if idx == len(candidate):
        return len(lines)
    else:
        maxV = 0
        # 尝试向当前结果中添加第idx条线
        curL = candidate[idx]
        joins = []
        elements = []
        for i in range(len(lines)):
            line = lines[i]
            # 如果发现相交
            if (curL[0]-line[0])*(curL[1]-line[1]) <= 0:
                joins.append(i)


        # 不添加当前线
        temp = dfs(candidate, lines, idx + 1)
        if temp > maxV:
            maxV = temp

        # 添加当前线
        # 直接添加
        if len(joins) == 0:
            lines.append(curL)
        else:
            # 先移除相交线再添加
            for j in range(len(joins)-1, -1, -1):
                elements.append(lines.pop(joins[j]))
            lines.append(curL)
        temp = dfs(candidate, lines, idx + 1)
        if temp > maxV:
            maxV = temp
        # 回溯
        lines.pop()
        if len(joins) != 0:
            # 先移除相交线再添加
            for j in range(len(joins)):
                lines.insert(joins[j], elements[len(joins)-1-j])
        return maxV


# 转换成最长公共子序列问题使用动态规划
def maxUncrossedLines(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: int
    """
    n = len(nums1)
    m = len(nums2)
    # n * m
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    # 遍历text1的字符
    for i in range(1, n + 1):
        # 遍历text2的字符
        for j in range(1, m + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


if __name__ == "__main__":
    nums1 = [1,4,2]
    nums2 = [1,2,4]
    print maxUncrossedLines(nums1, nums2)






