# coding=utf-8

import collections
def topKFrequent(words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    # 先统计所有单词出现的频率
    hashMap = collections.Counter(words)
    # 分别得到单词和数量
    word = hashMap.keys()
    num = hashMap.values()
    # 对数字进行堆排序

    length, n = len(num), len(num)
    # 首先构建大顶堆
    BuildMaxHeap(num, word, length)
    # 逐步对根节点下沉
    while length > n-k:
        length -= 1
        # 根节点与最后一个元素交换
        swap(num, word, 0, length)
        Sink(num, word, 0, length)


    return word[-k:][::-1]

# 建大顶堆
def BuildMaxHeap(nums, words, n):
    # 倒着从最后一个非叶子节点开始，对每个父节点进行下沉操作
    for i in range(n - 1, -1, -1):
        # 判断是不是叶子节点，如果不是叶子节点才执行下沉操作
        if 2 * i + 1 < n:
            Sink(nums, words, i, n)
    return

# 下沉操作
def Sink(nums, words, index, n):
    # 循环 直到不再需要下沉
    while True:
        # 左子节点
        j = 2 * index + 1
        # 两个子节点中选择更大的那个
        if j < n - 1 and (nums[j] < nums[j + 1] or (nums[j] == nums[j+1] and words[j] > words[j+1])):
            j += 1

        # 当前根节点下沉
        if j < n and (nums[index] < nums[j] or (nums[index] == nums[j] and words[index] > words[j])):
            swap(nums, words, index, j)
        else:
            break
        # 当前待下沉的元素所在位置
        index = j

    return


# 数组两个位置交换值
def swap(arr1, arr2, i, j):
    temp = arr1[i]
    arr1[i] = arr1[j]
    arr1[j] = temp

    temp = arr2[i]
    arr2[i] = arr2[j]
    arr2[j] = temp