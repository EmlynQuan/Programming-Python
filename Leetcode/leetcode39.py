# coding=utf-8
from collections import defaultdict

def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    # 对数组先排序
    candidates.sort()
    if target < candidates[0]:
        return []
    elif target == candidates[0]:
        return [[candidates[0]]]
    # 动态规划
    dp = defaultdict(set)
    # 备选项
    for candidate in candidates:
        dp[candidate] = [[candidate]]

    # 对比target小的数字遍历
    for i in range(candidates[0]+1, target+1):
        if i not in dp.keys():
            dp[i] = []
        # 遍历
        left, right = 1, i-1
        while left <= right:
            # 如果存在
            if left in dp.keys() and right in dp.keys():
                leftValue = dp[left]
                rightValue = dp[right]
                # 左右组合之后添加到对应位置
                for arrL in leftValue:
                    for arrR in rightValue:
                        temp = []
                        for x in arrL:
                            temp.append(x)
                        for x in arrR:
                            temp.append(x)
                        # 便于之后去重
                        temp.sort()
                        dp[i].append(temp)
            left += 1
            right -= 1

        # 对dp[i]去重
        temp = dp[i]
        idx = 1
        while idx < len(temp):
            pos = idx - 1
            # 和前面的相比
            while pos >= 0:
                # 判断两个数组重复
                if temp[idx] == temp[pos]:
                    temp.pop(idx)
                    idx -= 1
                    break
                pos -= 1
            idx += 1

    return dp[target]



