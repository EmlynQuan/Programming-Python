# coding=utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    '''
    找最近祖先
    '''
    ancestor = {}
    level = {}
    if root:
        findAncestor(root, ancestor, level, 0)

    # 如果是相同祖先
    if p.val == q.val:
        return ancestor[p.val]
    # 祖先是q
    if p.val in ancestor and q == ancestor[p.val]:
        return q
    # 祖先是p
    if q.val in ancestor and p == ancestor[q.val]:
        return p

    counter = 0
    # 递归去找祖先
    while True:
        if p == q:
            return p
        # q的更深
        pKey = p.val
        qKey = q.val

        if level[pKey] < level[qKey]:
            q = ancestor[qKey]
        # p的更深
        elif level[pKey] > level[qKey]:
                p = ancestor[pKey]
        # 相同的深度
        else:
            p = ancestor[pKey]
            q = ancestor[qKey]
        counter += 1
    return p


def findAncestor(self, root, ancestor, level, curLevel):
    level[root.val] = curLevel
    if root.left:
        ancestor[root.left.val] = root
        self.findAncestor(root.left, ancestor, level, curLevel+1)
    if root.right:
        ancestor[root.right.val] = root
        self.findAncestor(root.right, ancestor, level, curLevel+1)