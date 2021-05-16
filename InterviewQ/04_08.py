from collections import defaultdict

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if p == root or q == root:
        return root
        # 建立哈希表
    hashMap = defaultdict(TreeNode)
    hashMap[root] = None
    trav(root, hashMap)

    pFather = []
    qFather = []

    while p != None:
        pFather.append(p)
        p = hashMap[p]
    while q != None:
        qFather.append(q)
        q = hashMap[q]

    idx_p = len(pFather) - 1
    idx_q = len(qFather) - 1

    # 从后遍历
    while idx_p >= 0 and idx_q >= 0:
        if pFather[idx_p].val == qFather[idx_q].val:
            idx_p -= 1
            idx_q -= 1
        else:
            break

    return pFather[idx_p+1]


def trav(root, map):
    if root == None:
        return
    else:
        if root.left:
            map[root.left] = root
        if root.right:
            map[root.right] = root

        trav(root.left, map)
        trav(root.right, map)