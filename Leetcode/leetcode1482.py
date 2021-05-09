# coding=utf-8

def minDays(bloomDay, m, k):
    n = len(bloomDay)
    if m * k > n:
        return -1

    # 二分搜索
    left = min(bloomDay)
    right = max(bloomDay)
    if judge(bloomDay, right, m, k) == False:
        return -1
    while left < right:
        mid = (left + right) // 2
        # 中间可以
        # print mid
        if judge(bloomDay, mid, m, k):
            right = mid
        # 中间值也不满足
        else:
            left = mid+1

    return right


def judge(arr, value, m, k):
    counterM, counterK, i, flowers = 0, 0, 0, 0
    for t in arr:
        if t <= value:
            counterK += 1
            if counterK == k:
                counterM += 1
                if counterM == m:
                    return True
                counterK = 0
        else:
            counterK = 0
    return False


if __name__ == "__main__":
    bloomDay = [1000000000,1000000000]
    m = 1
    k = 2
    print minDays(bloomDay, m, k)
