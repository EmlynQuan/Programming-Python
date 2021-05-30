# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    pArr = []
    qArr = []
    ancestorP, ancestorQ = root, root
    # 利用二叉搜索树
    while ancestorP:
        if ancestorP.val < p.val:
            pArr.append(ancestorP)
            ancestorP = ancestorP.right
        elif ancestorP.val > p.val:
            pArr.append(ancestorP)
            ancestorP = ancestorP.left
        else:
            pArr.append(ancestorP)
            ancestorP = None
    while ancestorQ:
        if ancestorQ.val < q.val:
            qArr.append(ancestorQ)
            ancestorQ = ancestorQ.right
        elif ancestorQ.val > q.val:
            qArr.append(ancestorQ)
            ancestorQ = ancestorQ.left
        else:
            qArr.append(ancestorQ)
            ancestorQ = None

    idxP, idxQ = 0, 0
    while idxP < len(pArr) and idxQ < len(qArr):
        # print(pArr[idxP].val)
        print(qArr[idxQ].val)
        if pArr[idxP].val == qArr[idxQ].val:
            idxP += 1
            idxQ += 1
        else:
            break

    return pArr[idxP - 1]


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    lowestCommonAncestor_simple(root, root.left, root)