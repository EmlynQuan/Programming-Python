# coding=utf-8

def nextPermutation(nums):
    if len(nums) <= 1:
        return nums

    n = len(nums)
    # 从后面找一个大的值 交换位置 对这一段重新按升序排列
    for i in range(n-2, -1, -1):
        # 后面的值小于前面的值
        if nums[i+1] > nums[i]:
            for j in range(n-1, i, -1):
                # 较小的较大值
                if nums[j] > nums[i]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp

                    # 重新排列后面这部分
                    left = i+1
                    right = n-1
                    while left < right:
                        temp = nums[left]
                        nums[left] = nums[right]
                        nums[right] = temp
                        left += 1
                        right -= 1

                    return nums


    return nums.sort()


if __name__ == "__main__":
    # nums = [1,23,12,34,6,4,32]
    nums = [1,3,2]
    # [3, 2, 1]
    # [1, 1, 5]
    print nextPermutation(nums)