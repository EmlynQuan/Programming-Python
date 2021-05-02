# coding=utf-8

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    '''
    给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
    '''
    arr = []
    midOrder(root, arr, k)
    return arr[k-1]

def midOrder(root, arr, k):
    '''
    中序遍历
    '''
    if root:
        if len(arr) == k:
            return
        else:
            midOrder(root.left, arr, k)
            arr.append(root.val)
            midOrder(root.right, arr, k)
    return

if __name__ == "__main__":
    n2 = TreeNode(2, None, None)
    n1 = TreeNode(1, None, n2)
    n4 = TreeNode(4, None, None)
    n3 = TreeNode(3, n1, n4)

    print kthSmallest(n3, 1)

