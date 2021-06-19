# coding=utf-8

class Solution(object):
    def verifyPostorder(self, postorder):
        """
        判断序列是否为某个二叉搜索树的后序遍历序列
        :type postorder: List[int]
        :rtype: bool
        """
        return self.judgeTree(arr=postorder)

    def judgeTree(self, arr):
        if len(arr) == 0:
            return True
        else:
            # 无论有没有子节点 一定是存在根节点的
            root = arr[-1]
            # 从根节点往前找，找到第一个不大于根值的位置认为是左右子树的分界点
            right = []
            left = []
            flag = True
            for j in range(len(arr)-1):
                if arr[j] < root:
                    # 说明不符合规范
                    if flag == False:
                        return False
                    left.append(arr[j])
                else:
                    flag = False
                    right.append(arr[j])
            return self.judgeTree(left) and self.judgeTree(right)



