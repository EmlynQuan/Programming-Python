# coding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    if l1 == None:
        return l2
    if l2 == None:
        return l1

    newHeader = ListNode(0)
    pos = newHeader
    while l1 and l2:
        if l1.val < l2.val:
            pos.next = l1
            pos = pos.next
            l1 = l1.next
        else:
            pos.next = l2
            pos = pos.next
            l2 = l2.next

    while l1:
        pos.next = l1
        pos = pos.next
        l1 = l1.next
    while l2:
        pos.next = l2
        pos = pos.next
        l2 = l2.next

    pos.next = None
    return newHeader.next
