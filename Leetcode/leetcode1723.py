# coding=utf-8


# 无效方法
# 测试样例 [5,5,4,4,4]2
def minimumTimeRequired_1(jobs, k):
    # 对工作时间排序
    jobs.sort()
    time = [0 for _ in range(k)]
    minIdx = 0
    for i in range(len(jobs)-1, -1, -1):
        time[minIdx] += jobs[i]
        minValue = time[0]
        minIdx = 0
        for j in range(k):
            if minValue > time[j]:
                minValue = time[j]
                minIdx = j

    maxValue = float('-inf')
    for i in range(k):
        if maxValue < time[i]:
            maxValue = time[i]

    return maxValue


# 二分查找 + 回溯 + 剪枝
def minimumTimeRequired(jobs, k):
    # 对工作时间排序
    jobs.sort()
    # 二分查找的下限是最大的工作量 上限是全部的工作量之和
    right = sum(jobs)
    left = jobs[-1]
    n = len(jobs)


    while left < right:
        mid = (left + right) // 2
        # 当前值可行
        if checkTA(mid, jobs, n, k):
            right = mid
        # 不可行
        else:
            left = mid + 1
    return right

# 判断分配是否满足所有工人的最大工作时间
def checkTA(value, jobs, n, k):
    times = [0 for _ in range(k)]
    return dfs(value, jobs, times, n-1, k)

def dfs(value, jobs, times, i, k):
    # 已经全部分配完
    if i < 0:
        return True
    # 还有未分配的工作
    else:
        j = 0
        while j < k:
            if times[j] + jobs[i] <= value:
                # 分配给他
                times[j] += jobs[i]
                if dfs(value, jobs, times, i - 1, k):
                    return True
                # 回溯 撤销
                times[j] -= jobs[i]

            # 如果当前工人未被分配工作，那么下一个工人也必然未被分配工作
            # 或者当前工作恰能使该工人的工作量达到了上限
            # 这两种情况下我们无需尝试继续分配工作
            if times[j] == 0 or times[j] + jobs[i] == value:
                break
            # 给其他工人分配
            j += 1
        return False



if __name__ == "__main__":
    jobs = [254,256,256,254,251,256,254,253,255,251,251,255]
    k = 10

    print minimumTimeRequired(jobs, k)





