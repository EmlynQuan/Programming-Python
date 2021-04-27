# coding=utf-8

# 1。 求局部极小值
# 一个给定的不包含相同元素的整数数组，每个局部极小值的定义就是一个值比它左右相邻的都小的值，求这个数组的一个局部极小值
# 局部极小值一定是存在的，因为全局最小值就是一个解 可以有多个所以我们找一个就行
# 用二分的思想 (以下两题也使用二分思想去解决)
# a) 循环有序数组最小值，查找元素x （leetcode 153,154）
# b) 一个严格单增的数组，查找a[x] == x的位置


# 2。第一个缺失的正整数
# 给一个数组，找到从1开始，第一个不在里面的正整数（leetcode 4）
# 比如[3,4,-1,1] 输出2
# 思路 数组下标从0开始 那么构造a[i] = i+1 这样的逻辑，每次循环 要么i++ 要么n-- 要么有一个数被放到了正确的位置
def firstMissingPositive(arr):
    curPos = 0
    length = len(arr)
    while curPos < length:
        # 如果满足a[i] = i+1 则向后移动
        if arr[curPos] == curPos + 1:
            curPos += 1
        # 如果这个数大于数组长度或者是之前出现过的数字或者那个位置已经存在了则无意义
        elif arr[curPos] > length or arr[curPos] <= curPos or arr[arr[curPos]-1] == arr[curPos]:
            length -= 1
            arr[curPos] = arr[length]
        # 如果二者不相等就去找对应值的位置进行交换
        else:
            swap(arr, curPos, arr[curPos]-1)
    return curPos+1

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

# 3。给定一个排序数组，删除所有相同的元素，返回不同的值的个数K，同时将其按序移动到数组前K个位置，不允许开辟新的空间
# 思路是使用两个指针去指向当前位置和不同元素的位置
def deleteDuplicates(arr):
    if len(arr) == 0:
        return 0
    counter,i,j = 1,1,0
    # 尚未遍历完
    while i < len(arr) and j < len(arr)-1:
        # 当前j和其后j+1不同
        if arr[j] != arr[j+1]:
            arr[i] = arr[j+1]
            i += 1
            j += 1
            counter += 1
        # 当前元素和下一个元素是相同的
        else:
            j += 1
    return counter

# 4。元素最大间距离，给定一个整数数组（n>1）求把这些整数博鳌是在数轴上，相邻两个数差的最大值 （Leetcode 164）
# 划分成n+1个桶，每个桶的大小是d = (x-y)/(n+1) 浮点数
# 把所有数全部放到桶里，每个桶区间是[y+i*d, y+(i+1)*d) (i=0,1,2,……,n) 最后一个桶双闭区间
# 最小的数一定是在0号桶里，最大的数一定是在n号桶里， 首尾两个桶都非空
# 中间有空桶，空桶左右两侧肯定有元素，最大间隙出现在一个非空桶的最大值和下一个非空桶的最小值之间
# 判断数r在哪个桶里？ (r-y)*(n+1)/(x-y) (整数运算 下取整)  ps: r==x时结果取n
# 记录每个桶的最大值和最小值即可 时间空间都是o(n)
# def findMaxGap(arr):


# 5。只出现1次的数：一个数组，所有元素都出现了两次，只有两个数只出现了一次，求这两个数
# 所有数做异或 出现两次的数相抵消 最终的结果就是那两个出现1次的数x,y的异或结果 且非0


if __name__ == "__main__":
    # arr = [0,1,1,1,2,2,3,4,5,6,7,7,7,8,9,10,10]
    # print deleteDuplicates(arr)
    # print arr
    arr = [3,4,5,0,2,7,8,10-1,1]
    print firstMissingPositive(arr)
    print arr