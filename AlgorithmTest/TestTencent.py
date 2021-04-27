# coding=UTF-8

#一面：1。中序遍历二叉树
class Node():
    def __init__(self, value):
        self.value = value
        self.lChild = None
        self.rChild = None

    def addLeftChild(self, node):
        self.lChild = node

    def addRightChild(self, node):
        self.rChild = node

    def __str__(self):
        return str(self.value)

class Tree():
    def __init__(self, root):
        self.root = root

def trav(root):
    # 中序
    if root:
        # 左
        trav(root.lChild)
        # 根
        print(root)
        # 右
        trav(root.rChild)
    else:
        return

# 一面：2。跳跃 动态规划
def jump(arr):
    # 标记步数
    num = [0 for _ in range(0,len(arr))]
    num[-1] = 1

    for i in range(len(arr)-1, 0, -1):
        # 可以跳到最后
        if arr[i - 1] > len(arr) - 1 - i:
            num[i-1] = 1
        # 只能跳到中间
        else:
            min = 100
            # 遍历可以跳的位置
            for j in range(1,arr[i-1]+1):
                # 可达
                if num[i-1+j] != 0:
                    # 更小 更新
                    if num[i-1+j] + 1 < min:
                        min = num[i-1+j] + 1

            if min != 100:
                num[i-1] = min
    print(num[0])


# jump优化 贪心方法 时间复杂度达o(N)
def jumpOpt(arr):
    # 最大步数
    maxPos = 0
    # 步数
    steps = 0
    # 边界
    end = 0
    # 从左到右遍历 不需要遍历最后一个元素 到最后就直接跳出了
    for i in range(0, len(arr)-1):
        maxPos = max(maxPos, i+arr[i])
        # 到达上次跳跃能到达的右边界了
        if i == end:
            end = maxPos    # 目前能跳到的最远位置变成了下次起跳位置的有边界
            steps += 1      # 进入下一次跳跃
    return steps

# 二面：1。翻转句子中的单词
def reverse_word(word):
    words = word.split(" ")
    result = ""
    for i in range(len(words)):
        if i != 0:
            result += " "
        result += reverse(words[i])
    return result

# 对单词倒序
def reverse(word):
    arr = list(word)
    left = 0
    right = len(arr)-1

    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    return ''.join(arr)

# 二面：2。只翻转单词的前后顺序，不翻转单词内部顺序
def reverse(words):
    # 分割成单词
    arr = words.split(" ")
    left = 0
    right = len(arr)-1

    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    result = ""
    for i in range(len(arr)):
        if i != 0:
            result += " "
        result += arr[i]
    return result


# 二面：3。不同路径 动态规划
def findPath(grid,m,n):
    # 记录当前位置可以有几条路径到达
    dp = [[0 for _ in range(m)] for _ in range(n)]
    # 边界条件判断
    if grid[0][0] == 1:
        return -1
    if grid[m-1][n-1] == 1:
        return -1

    # 初始化两个位置的路径数
    if grid[m-2][n-1] == 0:
        dp[m-2][n-1] = 1
    if grid[m-1][n-2] == 0:
        dp[m-1][n-2] = 1

    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if grid[m-1][n-1] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[0][0]

# 三面 ipv4 32位
# import io
# import sys
# import math
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# #str = input()
# #print(str)
#
# str = input()
# str.replace(" ","")
# strList = str.split(".")
# # print(strList)
# sum = 0
# # 遍历
# for i in range(0, 4):
#     # 当前数字
#     temp = int(strList[i])
#     # print(temp)
#     # 遍历每一位
#     for j in range(0, 8):
#         value = temp & 0x00000001
#         # print(value)
#         if value == 1:
#             sum += math.pow(2, j)*math.pow(2, (3-i)*8)
#         temp >>= 1
#
# sum = int(sum)
# print(sum)
# print('hello world!')


def moveChar(str):
    arr = list(str)
    # pos是大写字母应该移动到的位置
    pos = len(arr)-1
    i = len(arr)-1
    while i >= 0:
        # 如果是大写字母
        if arr[i].isupper():
            temp = arr[i]
            j = i
            while j < pos:
                arr[j] = arr[j+1]
                j += 1
            arr[pos] = temp
            pos -= 1
        i -= 1

    return ''.join(arr)


    '''
    arr = list(str)
    bigIndex = 0
    pos = 0

    # 遍历
    while bigIndex < len(arr) and pos < len(arr):
        # 当前位置是小写字母
        if ord(arr[pos]) >= ord('a') and ord(arr[pos]) <= ord('z'):
            # 前面没有大写字母
            if pos <= bigIndex:
                pos += 1
            # 只需交换两个位置即可
            elif pos - bigIndex == 1:
                temp = arr[pos]
                arr[pos] = arr[bigIndex]
                arr[bigIndex] = temp
                bigIndex = pos
                pos += 1
            # 有多个大写字母,插入排序
            else:
                value = arr[pos]
                idx = pos
                while idx > bigIndex:
                    arr[idx] = arr[idx-1]
                    idx -= 1
                arr[idx] = value
                bigIndex = idx + 1
                pos += 1
        # 是大写字母
        else:
            # bigIndex = pos
            pos += 1

    return ''.join(arr)
    '''


def HuiWenString(str):
    arr = list(str)
    subLen = []

    for i in range(len(arr)):
        subLen.append([])
        for j in range(len(arr)):

            if i == j:
                subLen[i].append(1)
            else:
                subLen[i].append(0)

    # subLen[i][j] 表示下标i到下标j的最长回文传长度
    for i in range(len(arr)-1, -1,-1):
        for j in range(i+1,len(arr)):
            # 如果是对角线则为1 i== j时 也是回文串
            if i == j:
                subLen[i][j] = 1
            # 不相等时
            else:
                # 相等
                if arr[i] == arr[j]:
                    if j - i == 1:
                        subLen[i][j] = 2
                    else:
                        subLen[i][j] = subLen[i+1][j-1] + 2
                # 不等的话就是子串的最大
                else:
                    subLen[i][j] = max(subLen[i+1][j], subLen[i][j-1])

    return subLen[0][len(arr)-1]


# 数组逆序对
def mergeSort(self, nums, tmp, l, r):
    if l >= r:
        return 0

    mid = (l + r) // 2
    inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
    i, j, pos = l, mid + 1, l
    while i <= mid and j <= r:
        if nums[i] <= nums[j]:
            tmp[pos] = nums[i]
            i += 1
            inv_count += (j - (mid + 1))
        else:
            tmp[pos] = nums[j]
            j += 1
        pos += 1
    for k in range(i, mid + 1):
        tmp[pos] = nums[k]
        inv_count += (j - (mid + 1))
        pos += 1
    for k in range(j, r + 1):
        tmp[pos] = nums[k]
        pos += 1
    nums[l:r + 1] = tmp[l:r + 1]
    return inv_count

def reversePairs(self, nums):
    n = len(nums)
    tmp = [0] * n
    return self.mergeSort(nums, tmp, 0, n - 1)


if __name__ == "__main__":
    test = "google"
    print HuiWenString(test)
    # root = Node(1)
    # root.addLeftChild(Node(2))
    # root.addRightChild(Node(3))
    # lc = root.lChild
    # lc.addLeftChild(Node(4))
    # test = Tree(root)
    #
    # print("=============")
    # trav(test.root)

    # test = [1,2,3,4,5,6,7,8,9]
    # print(jumpOpt(test))


    # test = "I am a student."
    # print(reverse(test))

    # m = 4
    # n = 4
    # grid = [[0 for _ in range(m)] for _ in range(n)]
    # # for i in range(m):
    # #     for j in range(n):
    # #         if i == j and i != m-1:
    # #             grid[i][j] = 1
    # grid[1][1] = 1
    # grid[2][2] = 1
    #
    # # print grid
    # print (findPath(grid, m, n))

    str = "AkleBiCeilD"
    print str
    print moveChar(str)



'''
腾讯笔试

# coding=UTF-8
import sys
import math

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        print self.val
        # print self.left
        print self.right
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 你需要返回一个指针，指向root，表示删减去若干个点后，剩下的树
# @param root TreeNode类 指向二叉树的根
# @return TreeNode类
#
# class Solution:
#     def solve(self, root):

def bulidTree(arr, root, i):
    # 建左子树
    if 2*i+1 < len(arr):
        root.left = TreeNode(arr[2*i+1])
        bulidTree(arr, root.left, 2 * i + 1)
    # 建右子树
    if 2*i+2 < len(arr):
        root.right = TreeNode(arr[2*i+2])
        bulidTree(arr, root.right, 2 * i + 2)
    return root

def test():
    str = sys.stdin.readline().strip()
    str = str.replace("{", "")
    str = str.replace("}", "")
    arr = str.split(",")

    # 找到当前最前的'#'
    i = 0
    while i < len(arr):
        if arr[i] == '#':
            break
        else:
            arr[i] = int(arr[i])
        i += 1

    level = int(math.log(i + 1, 2))
    length = int(math.pow(2, level)) - 1
    arr = arr[0:length]

    if len(arr) > 0:
        root = TreeNode(x=arr[0])
    else:
        root = TreeNode(x=None)
    bulidTree(arr, root, 0)
    print root


def test2():
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    arr = []
    for i in range(n):
        arr.append(int(line[i]))
    left = 0
    right = 1
    while left >= 0 and right < len(arr):
        # 消除
        if arr[left] + arr[right] == 10:
            arr.pop(left)
            arr.pop(left)
            if left >= 1:
                left -= 1
                right -= 1
        else:
            left += 1
            right += 1

    print(len(arr))


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(arr, left, right):
    index = right
    value = arr[right]
    i = left
    while i < index:
        if arr[i] > value:
            index -= 1
            swap(arr, i, index)
        else:
            i += 1

    swap(arr, index, right)
    return index


def quickSort(arr, l, r):
    if l >= r:
        return
    else:
        index = partition(arr, l, r)
        quickSort(arr, l, index-1)
        quickSort(arr, index+1, r)

# # 首先排序，再两两分组
# def test3(arr):
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        counter = int(sys.stdin.readline().strip())
        arr = list(map(int, sys.stdin.readline().split()))
        quickSort(arr, 0, len(arr)-1)

        ret = 0
        # 多个奇数个
        if len(arr) % 2 != 0:
            for i in range(0, (len(arr)+1)//2):
                ret += arr[2*i]
            # 计算返回的
            for i in range(len(arr) // 2):
                ret += arr[i+1]
        else:
            for i in range(0, len(arr)//2):
                ret += arr[2*i+1]
            # 计算返回的
            for i in range(len(arr) // 2):
                ret += arr[i]
        print(ret)

#
# if __name__ == "__main__":

'''