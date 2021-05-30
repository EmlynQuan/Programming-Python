# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def kthLargest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    ret = []
    getOrder(root, ret)
    return ret[-k]

def getOrder(root, ans):
    if root == None:
        return
    if root.left:
        getOrder(root.left, ans)
    ans.append(root.val)
    if root.right:
        getOrder(root.right, ans)


def kthLargest_NR(root, k):
    if not root:
        return
    stack = []
    seq = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        seq.append(root.val)
        root = root.right
    return seq[-k]