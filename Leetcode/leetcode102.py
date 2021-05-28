# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root == None:
        return []
    ret = [[root.val]]
    queue = [root]
    counter, nextCounter = 1,0
    while queue:
        temp = queue.pop(0)
        ret[-1].append(temp.val)
        counter -= 1

        if temp.left:
            queue.append(temp.left)
            nextCounter += 1
        if temp.right:
            queue.append(temp.right)
            nextCounter += 1
        if counter == 0:
            if nextCounter != 0:
                ret.append([])
            counter = nextCounter
            nextCounter = 0
    return ret


