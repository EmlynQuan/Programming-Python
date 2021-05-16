
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isCousins(root, x, y):
    """
    :type root: TreeNode
    :type x: int
    :type y: int
    :rtype: bool
    """
    if x.val == 1 or y.val == 1:
        return False

    x_f, x_l, _ = getFather(root, x.val, 0)
    y_f, y_l, _ = getFather(root, y.val, 0)

    if x_l == y_l and x_f != y_f:
        return True
    else:
        return False

def getFather(root, value, level):
    if root == None:
        return None, None, False
    if root.left:
        if root.left.val == value:
            return root, level+1, True
        else:
            temp, l, flag = getFather(root.left, value, level+1)
            if flag:
                return temp, l, flag
    if root.right:
        if root.right.val == value:
            return root, level + 1, True
        else:
            temp, l, flag = getFather(root.right, value, level + 1)
            if flag:
                return temp, l, flag

    return None, None, False
