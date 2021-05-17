# coding=utf-8

def smallestK(arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: List[int]
    """
    # 建堆
    buildMinHeap(arr)
    # 逐步对根节点下沉
    length = len(arr)
    while length > len(arr) - k:
        length -= 1
        # 根节点与最后一个元素交换
        temp = arr[0]
        arr[0] = arr[length]
        arr[length] = temp
        sink(arr, 0, length)

    return arr[-k]


# 建小顶堆
def buildMinHeap(arr):
    # 倒着从最后一个非叶子节点开始，对每个父节点进行下沉操作
    for i in range(len(arr) - 1, -1, -1):
        # 判断是不是叶子节点，如果不是叶子节点才执行下沉操作
        if 2 * i + 1 < len(arr):
            sink(arr, i, len(arr))

# 下沉操作
def sink(arr, index, len):
    # 循环 直到不再需要下沉
    while True:
        # 左子节点
        j = 2 * index + 1
        # 两个子节点中选择更大的那个
        if j < len - 1 and arr[j] > arr[j + 1]:
            j += 1

        # 当前根节点下沉
        if j < len and arr[index] > arr[j]:
            temp = arr[index]
            arr[index] = arr[j]
            arr[j] = temp
        else:
            break

        # 当前待下沉的元素所在位置
        index = j
