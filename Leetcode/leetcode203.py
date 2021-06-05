# coding=utf-8

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        newHead = ListNode(0)
        newHead.next = head
        pre, cur = newHead, head

        while head:
            # 删除当前节点
            if head.val == val:
                pre.next = head.next
                head = head.next
            else:
                pre = head
                head = head.next

        return newHead.next


