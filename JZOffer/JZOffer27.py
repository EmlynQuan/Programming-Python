# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mirrorTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root == None:
        return root
    queue = [root]
    while queue:
        temp = queue[0]
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
        node = temp.left
        temp.left = temp.right
        temp.right = node
        queue.pop(0)

    return root

