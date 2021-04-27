# coding=utf-8
# 冒泡排序
def BubbleSort(arr):
    # 对 [0,n-1]的元素 执行与其后紧邻的元素交换
    size = len(arr)
    flag = 0
    # 外层循环的是当前有序元素的个数 如果当前size-1个有序 则经过冒泡交换的剩余的1个也一定是有序的
    for i in range(0, size-1):
        # 内层循环的是需要相邻之间比较的元素的下表
        for j in range(0, size-1-i):
            if (arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                flag = 1
        if flag == 0:
            return

# 选择排序
def SelectSort(arr):
    # 从无序的数组中选择最小的元素放到有序数组的末尾
    size = len(arr)
    for i in range(0, size-1):
        minIndex = -1
        minValue = float('inf')
        for j in range(i, size-1):
            if arr[j] < minValue:
                minValue = arr[j]
                minIndex = j
        # 找到最小值 与当前的i位置元素交换
        arr[minIndex] = arr[i]
        arr[i] = minValue

# 插入排序
def InsertSort(arr):
    # 按顺序将未排序数组中的元素逐个插入到前面有序数组中
    # 默认第一个元素为有序数组
    size = len(arr)
    # 外层循环是当前尚未排序的起始位置索引遍历
    for i in range(1, size):
        # 当前要插入的元素值
        temp = arr[i]
        j = i-1
        # 内层循环是从后往前依次找应该插入的位置，找的过程中同时要移动元素
        while j >= 0:
            if arr[j] > temp:
                arr[j+1] = arr[j]
                j = j - 1
            else:
                break
        # 找到需要插入的位置是j和j+1之间 但j+1已经往后移动了 (因为此时最后一个找到后已经把j变成了j-1)
        arr[j+1] = temp


# 快速排序
def quickSort(arr, left, right):
    # print arr
    if left > right:
        return
    else:
        # 基准元素的位置索引
        index = partition(arr, left, right)
        # print '左'
        quickSort(arr, left, index-1)
        # print '右'
        quickSort(arr, index+1, right)

# 交换元素
def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

# 分区 按照基准元素分割 将小于其的元素放在左边 大于其的元素放在右边
def partition(arr, left, right):
    # 随机选择的情况
    # index = random()
    # swap(arr, random(), right)
    index = right
    anchor = arr[right]
    i = left
    while i < index:
        if arr[i] > anchor:
            index = index - 1
            swap(arr, i, index)
        else:
            i = i+1
        # print arr[left:right]
        # print i
        # print index
    swap(arr, index, right)
    return index


# 归并排序
def MergeSort(arr):
    if len(arr) < 2:
        return arr
    else:
        # 将原始数组分成两个子序列
        # 分别对两个子序列进行归并排序
        idx = len(arr) // 2
        # print idx
        arr1 = MergeSort(arr[0:idx])
        arr2 = MergeSort(arr[idx:len(arr)])
        # 合并归并排序后的两个子序列
        return Merge(arr1, arr2)

# 将两个有序序列合并成一个序列
def Merge(arr1, arr2):
    # print 'Merge'
    # print arr1
    # print arr2
    result = []
    while len(arr1) > 0 and len(arr2) > 0:
        if (arr1[0] < arr2[0]):
            result.append(arr1[0])
            arr1 = arr1[1:]
        else:
            result.append(arr2[0])
            arr2 = arr2[1:]

    if len(arr1) > 0:
        result.extend(arr1)
    if len(arr2) > 0:
        result.extend(arr2)
    return result


# 堆排序
def HeapSort(arr):
    # 首先构建大顶堆
    BuildMaxHeap(arr)
    # 逐步对根节点下沉
    length = len(arr)
    while length > 1:
        length -= 1
        # 根节点与最后一个元素交换
        swap(arr, 0, length)
        Sink(arr, 0, length)

    return arr

# 创建最大堆
def BuildMaxHeap(arr):
    # 倒着从最后一个非叶子节点开始，对每个父节点进行下沉操作
    for i in range(len(arr)-1, -1, -1):
        # 判断是不是叶子节点，如果不是叶子节点才执行下沉操作
        if 2*i+1 < len(arr):
            Sink(arr, i, len(arr))

# 下沉操作
def Sink(arr, index, len):
    # 循环 直到不再需要下沉
    while True:
        # 左子节点
        j = 2*index+1
        # 两个子节点中选择更大的那个
        if j < len-1 and arr[j] < arr[j+1]:
            j += 1

        # 当前根节点下沉
        if j < len and arr[index] < arr[j]:
            swap(arr, index, j)
        else:
            break
        # 当前待下沉的元素所在位置
        index = j

# 数组两个位置交换值
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


if __name__ == "__main__":
    list = [1,21,3,44,65,5,79,13,89,34,257,57,32,4,67,34,63,99,213,1382]
    # BubbleSort(list)
    # print(list)
    # SelectSort(list)
    # print(list)
    # InsertSort(list)
    # print(list)
    # quickSort(list, 0, len(list) - 1)
    # print(list)
    # list = MergeSort(list)
    # print(list)
    list = HeapSort(list)
    print(list)