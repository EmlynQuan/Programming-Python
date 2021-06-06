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
    ret = [[]]
    queue = [root]
    counter, nextCounter = 1, 0
    while queue:
        # 从右到左
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

    for i in range(len(ret)):
        if i % 2 == 1:
            left, right = 0, len(ret[i])-1
            while left < right:
                temp = ret[i][left]
                ret[i][left] = ret[i][right]
                ret[i][right] = temp
                left += 1
                right -= 1
    return ret


