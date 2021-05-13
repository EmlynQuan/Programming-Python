# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def listOfDepth(tree):
    if tree == None:
        return []

    ret = []
    curNode = []

    myQueue = [tree]
    level, curCounter, nextCounter = 1, 1, 0
    while len(myQueue):
        root = myQueue.pop(0)

        if root.left:
            myQueue.append(root.left)
            nextCounter += 1
        if root.right:
            myQueue.append(root.right)
            nextCounter += 1

        # 需要建头
        if level > len(ret):
            head = ListNode(root.val)
            ret.append(head)
            curNode.append(head)
        else:
            curNode[level-1].next = ListNode(root.val)
            curNode[level-1] = curNode[level-1].next

        curCounter -= 1
        if curCounter == 0:
            level += 1
            curCounter = nextCounter
            nextCounter = 0

    return ret

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    listOfDepth(root)






