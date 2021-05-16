# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True

        val = node.val
        if val <= lower or val >= upper:
            return False

        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True

    return helper(root)



if __name__ == "__main__":
    root = TreeNode(98)
    root.left = TreeNode(-57)
    root.left.right = TreeNode(58)
    root.left.right.left = TreeNode(31)
    print isValidBST(root)