# coding=utf-8

def threeSumClosest(nums, target):
    # 先排序
    n = len(nums)
    nums.sort()
    value = float('inf')

    # 计算两数之和
    for i in range(n):
        left, right = i+1, n-1
        while left < n and right >= i+1:
            # print "================"
            # print i
            # print left
            # print right
            if left == right:
                break

            temp = nums[i] + nums[left] + nums[right]
            if temp == target:
                return target
            elif temp > target:
                right -= 1
            else:
                left += 1

            # 必须是三个不同的数
            if abs(value - target) > abs(temp - target):
                value = temp
            # print value

    return value


if __name__ == "__main__":
    nums = [-1,2,1,9,8,45,-4]
    print threeSumClosest(nums, 7)