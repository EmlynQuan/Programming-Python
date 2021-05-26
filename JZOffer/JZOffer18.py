# coding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    pre, cur = head, head
    if head == None:
        return None
    if head.val == val:
        return head.next
    while cur:
        if cur.val == val:
            pre.next = cur.next
            return head
        else:
            pre = cur
            cur = cur.next
    return head
