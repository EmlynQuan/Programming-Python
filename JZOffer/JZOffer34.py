# coding=utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        if root == None:
            return ret
        self.findPath(curRoot=root, ans=ret, path=[root.val], curSum=root.val, target=target)
        return ret

    def findPath(self, curRoot, ans, path, curSum, target):
        '''
        :param curRoot: 当前根节点
        :param ans: 最终需要返回的结果
        :param ans: 当前遍历的路径
        :param curSum: 当前和
        :param target: 目标和
        :return: None
        '''
        # 判断左子树
        if curRoot.left:
            curSum += curRoot.left.val
            path.append(curRoot.left.val)
            self.findPath(curRoot.left, ans, path, curSum, target)
            # 回溯
            curSum -= path.pop(-1)
        # 判断右子树
        if curRoot.right:
            curSum += curRoot.right.val
            path.append(curRoot.right.val)
            self.findPath(curRoot.right, ans, path, curSum, target)
            # 回溯
            curSum -= path.pop(-1)

        if curRoot.left == None and curRoot.right == None:
            if curSum == target:
                ans.append([x for x in path])



if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)

    print Solution().pathSum(root, 17)