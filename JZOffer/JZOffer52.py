# coding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    curA, curB = headA, headB
    flag = False
    while curA and curB:
        if curA == curB:
            return curB
        curA = curA.next
        curB = curB.next
        if curA == None:
            if flag:
                return None
            flag = True
            curA = headB
        if curB == None:
            curB = headA

