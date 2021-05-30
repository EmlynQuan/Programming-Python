# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    ancestorDict = {}
    if root == None:
        return None
    ancestorDict[root.val] = None
    getNodeAncestor(root, ancestorDict)

    pArr = []
    qArr = []
    while p or q:
        if p:
            pArr.append(p)
            p = ancestorDict[p.val]
        if q:
            qArr.append(q)
            q = ancestorDict[q.val]
    idxP, idxQ = len(pArr)-1, len(qArr)-1
    while idxP >= 0 and idxQ >= 0:
        if pArr[idxP].val == qArr[idxQ].val:
            idxP -= 1
            idxQ -= 1
        else:
            break

    return pArr[idxP + 1]


def getNodeAncestor(root, ancDict):
    if root == None:
        return
    if root.left:
        ancDict[root.left.val] = root
    if root.right:
        ancDict[root.right.val] = root
    getNodeAncestor(root.left, ancDict)
    getNodeAncestor(root.right, ancDict)
