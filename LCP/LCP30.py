# coding=utf-8

def magicTower(nums):
    n = len(nums)
    dp = [0 for i in range(n)]
    dp[0] = 1+nums[0]

    if sum(nums) < 0:
        return -1

    counter = 0
    for i in range(1, n):
        dp[i] += nums[i] + dp[i-1]
        if dp[i] < 0:
            pos = i
            temp = min(nums[0:i + 1])
            while pos >= 0:
                if nums[pos] == temp:
                    break
                pos -= 1
            # 把pos位置移到后面
            counter += 1
            for j in range(pos, i+1):
                dp[j] -= nums[i]


