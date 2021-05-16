# coding=utf-8

class Node:
    def __init__(self):
        self.left = None
        self.right = None

def findMaximumXOR(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 建立树
    root = Node()
    # 共31位 最高位的二进制位编号为 30
    HIGH_BIT = 30
    maxValue = 0
    # 遍历每个值搜索
    for i in range(1, len(nums)):
        # 将 nums[i-1] 放入字典树，此时 nums[0 .. i-1] 都在字典树中
        addNodeToTree(nums[i-1], root, HIGH_BIT)
        # 将 nums[i] 看作 ai，找出最大的 x 更新答案
        maxValue = max(maxValue, searchMaxValue(nums[i], root, HIGH_BIT))

    return maxValue

# 向树中添加节点
def addNodeToTree(root, num, bitNum):
    cur = root
    # 依次得到每一位 从高到低
    for k in range(bitNum, -1, -1):
        bit = (num >> k) & 1
        # 向左
        if bit == 0:
            if cur.left == None:
                cur.left = Node()
            cur = cur.left
        # 向右
        else:
            if cur.right == None:
                cur.right = Node()
            cur = cur.right

# 计算当前给定的值与树中存在的值的最大异或值 （从高位找二进制尽可能不同）
def searchMaxValue(root, num, bitNum):
    cur = root
    ans = 0
    # 依次得到当前位 从高到低
    for k in range(bitNum, -1, -1):
        bit = (num >> k) & 1
        # 当前位为1 尽可能向左搜索
        if bit == 1:
            if cur.left:
                cur = cur.left
                ans = 2*ans + 1
            else:
                cur = cur.right
                ans = 2*ans
        # 当前位为0 尽可能向右搜索
        else:
            if cur.right:
                cur = cur.right
                ans = 2*ans + 1
            else:
                cur = cur.left
                ans = 2*ans
    return ans