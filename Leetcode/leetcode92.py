# coding=utf-8

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




def reverseBetween(head, left, right):
    pos, preTail, revHead, nextHead = head, head, head, head
    counter = 0

    while pos:
        if counter == left-1:
            preTail = pos
        if counter == left:
            revHead = pos
        if counter == right:
            nextHead = pos.next
            pos.next = None
            break
        pos = pos.next
        counter += 1

    # 翻转
    newHead, newTail = reverse(revHead)
    if left == 1:
        newTail.next = nextHead
        return newHead
    else:
        preTail.next = newHead
        newTail.next = nextHead
        return head


def reverse(head):
    # 翻转的是一个节点
    if head.next == None:
        return head, head
    else:
        newHead = ListNode(0, None)
        p, q = head, head
        while p:
            q = p.next
            p.next = newHead.next
            newHead.next = p
            p = q

        return newHead.next, head


