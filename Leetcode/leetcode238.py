# coding=utf-8

def productExceptSelf(nums):
    n = len(nums)
    answer = [1 for _ in range(n)]

    # 遍历 获取当前索引左侧的乘积
    for i in range(1, n):
       answer[i] = answer[i-1]*nums[i-1]

    print answer
    R = 1
    # 遍历 获取当前索引右侧的乘积
    for i in range(n-2, -1, -1):
        R *= nums[i+1]
        answer[i] *= R

    return answer

if __name__ == "__main__":
    test = [1, 2, 3, 4]
    print productExceptSelf(test)