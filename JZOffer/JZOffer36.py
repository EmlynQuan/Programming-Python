# coding=utf-8

# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # head
        head, tail = root, root
        self.travTree(root.left, root, True)
        self.travTree(root.right, root, False)
        while head.left:
            head = head.left
        while tail.right:
            tail = tail.right

        head.left = tail
        tail.right = head
        return head

    def travTree(self, curNode, father, tempNode, leftFlag):
        if curNode == None:
            return
        else:
            # 如果当前已经是叶子了, 可以修改指针了
            if curNode.left == None and curNode.right == None:
                # 当前节点的右节点是父节点
                if leftFlag:
                    curNode.right = father
                    if curNode.val > tempNode.val:
                        tempNode = curNode
                # 当前节点的左节点是父节点
                else:
                    curNode.left = father
                    if curNode.val < tempNode.val:
                        tempNode = curNode
            else:
                # 如果还有左子节点
                if curNode.left:
                    self.travTree(curNode.left, curNode, tempNode, True)
                    curNode.left = tempNode
                    tempNode.right = curNode
                # 如果还有右子节点
                if curNode.right:
                    self.travTree(curNode.right, curNode, tempNode, False)
                    curNode.right = tempNode
                    tempNode.left = curNode


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    Solution().treeToDoublyList(root)