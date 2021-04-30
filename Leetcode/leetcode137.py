# coding=utf-8

# 暴力解法
def singleNumber(nums):
    for i in range(len(nums)):
        flag = False
        for j in range(len(nums)):
            if i != j:
                if nums[i] == nums[j]:
                    flag = True
                    break
        if flag == False:
            return nums[i]



# 哈希表解法
def singleNumber(nums):
    myDict = {}
    for i in range(len(nums)):
        if nums[i] in myDict.keys():
            myDict[nums[i]] += 1
        else:
            myDict[nums[i]] = 1

    for key in myDict.keys():
        if myDict[key] == 1:
            return key