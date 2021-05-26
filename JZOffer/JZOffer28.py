# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root == None:
        return True
    else:
        if root.left == None and root.right == None:
            return True
        elif root.left == None or root.right == None:
            return False
        elif root.left.val != root.right.val:
            return False
        else:
            leftQ, rightQ = [], []
            leftQ.append(root.left)
            rightQ.append(root.right)
            while leftQ and rightQ:
                temp1 = leftQ.pop(0)
                temp2 = rightQ.pop(0)
                if temp1.left and temp2.right:
                    if temp1.left.val == temp2.right.val:
                        leftQ.append(temp1.left)
                        rightQ.append(temp2.right)
                    else:
                        return False
                elif temp1.left == None and temp2.right != None or temp1.left != None and temp2.right == None:
                    return False
                if temp1.right and temp2.left:
                    if temp1.right.val == temp2.left.val:
                        leftQ.append(temp1.right)
                        rightQ.append(temp2.left)
                    else:
                        return False
                elif temp1.right == None and temp2.left != None or temp1.right != None and temp2.left == None:
                    return False
            return True


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    print isSymmetric(root)
