# coding=utf-8

# 动态规划
def deleteAndEarn(nums):
    maxNum = max(nums)
    mySum = [0 for _ in range(maxNum)]
    for num in nums:
        mySum[num-1] += num
    dp = [0 for _ in range(maxNum)]

    dp[0] = mySum[0]
    if maxNum > 1:
        dp[1] = max(dp[0], mySum[1])
    for i in range(2, maxNum):
        dp[i] = max(dp[i-2]+mySum[i], dp[i-1])
    return dp[-1]



if __name__ == "__main__":
    nums = [1]
    print deleteAndEarn(nums)