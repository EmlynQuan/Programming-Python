# coding=utf-8
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(root1, root2):
    if root1 == None and root2 == None:
        return True

    leafArr1, leafArr2 = [], []

    getLeaf(root1, leafArr1)
    getLeaf(root2, leafArr2)

    if len(leafArr1) != len(leafArr2):
        return False
    for i in range(len(leafArr1)):
        if leafArr1[i] != leafArr2[i]:
            return False

    return True


def getLeaf(root, arr):
    if root.left == None and root.right == None:
        arr.append(root.val)
    else:
        if root.left != None:
            getLeaf(root.left, arr)
        if root.right != None:
            getLeaf(root.right, arr)

