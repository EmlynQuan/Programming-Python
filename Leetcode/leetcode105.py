# coding=utf-8

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    '''
    通过给定的前序和中序遍历构建二叉树
    '''
    if len(preorder) > 0:
        # 根节点
        root = TreeNode(val=preorder[0])
        buildChildTree(root, preorder, inorder)
        return root
    else:
        return None

def buildChildTree(root, preArr, inArr):
    '''
    对指定的根节点 通过前序和中序遍历构建子树
    '''
    # print 'root'
    # print 'pre' + str(preArr)
    # print 'in' + str(inArr)
    # print '\n'
    # 结束条件
    if len(preArr) > 0:
        # 找当前根节点的左子树的所有节点
        leftNodeNum = 0
        for val in inArr:
            # 如果找到当前的根节点
            if val == preArr[0]:
                break
            else:
                leftNodeNum += 1

        # 左边的节点数
        if leftNodeNum > 0:
            # 构建左子节点 和对应的子树
            root.left = TreeNode(val=preArr[1])
            # 截取剩余有效的前序和中序
            buildChildTree(root.left, preArr[1:leftNodeNum + 1], inArr[:leftNodeNum])
        else:
            root.left = None

        # 截取剩余有效的前序和中序
        preArr = preArr[leftNodeNum + 1:]
        inArr = inArr[leftNodeNum + 1:]

        # 还有右子树
        if len(preArr) > 0:
            root.right = TreeNode(preArr[0])
            # 还有右子树
            if len(preArr) > 1:
                # 构建右子节点 和对应的子树
                rightPreArr = preArr
                buildChildTree(root.right, preArr, inArr)
        # 无右根
        else:
            root.right = None
    else:
        root.left = None
        root.right = None

if __name__ == "__main__":
    preArr = [3,9,20,15,7]
    inArr = [9,3,15,20,7]
    root = buildTree(preArr, inArr)
    print root


