# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None:
        return 0
    queue = [root]
    level = 0
    preCounter, curCounter = 1,0
    while queue:
        curNode = queue[0]
        if curNode.left:
            queue.append(curNode.left)
            curCounter += 1
        if curNode.right:
            queue.append(curNode.right)
            curCounter += 1
        queue.pop(0)
        preCounter -= 1
        if preCounter == 0:
            preCounter = curCounter
            curCounter = 0
            level += 1
    return level

