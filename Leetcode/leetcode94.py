# coding=utf-8


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    ret = []
    trav(root, ret)
    return ret


def trav(root, ans):
    if root:
        trav(root.left, ans)
        ans.append(root.val)
        trav(root.right, ans)