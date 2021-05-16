class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderSuccessor(root, p):
    """
    :type root: TreeNode
    :type p: TreeNode
    :rtype: TreeNode
    """
    ans = []
    trav(root, ans)
    # 二叉搜索树性质
    left, right = 0, len(ans) - 1
    idx = -1
    value = p.val
    while left <= right:
        if ans[left].val == value:
            idx = left
            break
        elif ans[left].val < value:
            left += 1
        else:
            break
        if ans[right].val == value:
            idx = right
            break
        elif ans[right].val > value:
            right -= 1
        else:
            break

    if idx == -1 or idx == len(ans) - 1:
        return None
    else:
        return ans[idx + 1]


def trav(root, ans):
    if root == None:
        return
    else:
        trav(root.left, ans)
        ans.append(root)
        trav(root.right, ans)

