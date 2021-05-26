# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root == None:
        return True
    # 左侧
    left, flagL = getTreeLevel(root.left)
    # 右侧
    right, flagR = getTreeLevel(root.right)

    if flagL and flagR:
        gap = left - right
        if -1 <= gap <= 1:
            return True
        else:
            return False
    else:
        return False


def getTreeLevel(root):
    if root == None:
        return 0, True
    else:
        left, flagL = getTreeLevel(root.left)
        right, flagR = getTreeLevel(root.right)
        if flagL == False or flagR == False:
            return 0, False
        else:
            maxLevel = max(left, right)
            minLevel = min(left, right)
            if maxLevel - minLevel <= 1:
                return maxLevel+1, True
            else:
                return 0, False