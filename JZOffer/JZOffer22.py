# coding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getKthFromEnd(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    # 找倒数第k个
    counter = 0
    cur,pre = head, head
    flag = False
    while cur:
        cur = cur.next
        if counter >= k:
            flag = True
            pre = pre.next
        counter += 1
    return pre