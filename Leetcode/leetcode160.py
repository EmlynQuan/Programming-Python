# coding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA, curB = headA, headB
        flag = False
        while curA and curB:
            if curA == curB:
                return curA
            else:
                if curA.next != None:
                    curA = curA.next
                else:
                    if flag:
                        return None
                    curA = headB
                    flag = True

                if curB.next != None:
                    curB = curB.next
                else:
                    curB = headA


