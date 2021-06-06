# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if B == None:
            return False
        queue = [A]
        while queue:
            temp = queue.pop(0)
            if temp.val == B.val:
                if self.judge(temp, B):
                    return True
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

        return False


    def judge(self, A, B):
        if B == None:
            return True
        elif A == None and B != None:
            return False
        else:
            if A.val != B.val:
                return False
            else:
                return self.judge(A.left, B.left) and self.judge(A.right, B.right)