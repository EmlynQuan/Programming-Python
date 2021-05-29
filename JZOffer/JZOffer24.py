# coding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None:
        return head

    pre, cur, newHead = head, head.next, head
    head.next = None
    while cur:
        pre = cur
        cur = cur.next
        pre.next = newHead
        newHead = pre

    return newHead

