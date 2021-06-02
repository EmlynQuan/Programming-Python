# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        # 前序的首字母是根节点
        root = TreeNode(preorder[0])
        # 根据当前的前序和中序去重建二叉树
        self.bulidCurTree(curRoot=root, preArr=preorder, inArr=inorder)
        return root

    def bulidCurTree(self, curRoot, preArr, inArr):
        if len(preArr) > 0:
            curRoot.val = preArr[0]
            # 存在有左/右孩子 或者二者都有
            if len(preArr) > 1:
                pos = 0
                # 找到左子树的所有序列
                while inArr[pos] != preArr[0]:
                    pos += 1
                # pos指向的位置是根节点在中序遍历数组中的位置
                curRoot.left = TreeNode(-1)
                curRoot.right = TreeNode(-1)
                # 构建左子树
                if self.bulidCurTree(curRoot=curRoot.left, preArr=preArr[1:pos+1], inArr=inArr[:pos]) == False:
                    curRoot.left = None
                # 构建右子树
                if self.bulidCurTree(curRoot=curRoot.right, preArr=preArr[pos+1:], inArr=inArr[pos+1:]) == False:
                    curRoot.right = None
            else:
                curRoot.left = None
                curRoot.right = None
                return True
        else:
            return False


if __name__ == "__main__":
    temp = Solution()
    pre = [1, 2]
    inA = [2, 1]
    temp.buildTree(preorder=pre, inorder=inA)