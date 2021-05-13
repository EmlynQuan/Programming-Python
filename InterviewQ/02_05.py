# coding=utf-8

class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = ListNode(0)
    curNode,preNode = head, head
    ca = 0

    if l1 == None:
        return l2
    if l2 == None:
        return l1

    while l1 and l2:
        if curNode == head:
            preNode = head
        else:
            preNode = curNode
        temp = l1.val + l2.val + ca
        ca = temp // 10
        curNode.val = temp % 10
        curNode.next = ListNode(0)
        curNode = curNode.next
        l1 = l1.next
        l2 = l2.next

    while l1 != None:
        preNode = curNode
        temp = l1.val + ca
        curNode.val = temp % 10
        ca = temp // 10
        curNode.next = ListNode(0)
        curNode = curNode.next
        l1 = l1.next

    while l2 != None:
        preNode = curNode
        temp = l2.val + ca
        curNode.val = temp % 10
        ca = temp // 10
        curNode.next = ListNode(0)
        curNode = curNode.next
        l2 = l2.next

    if ca != 0:
        curNode.val = ca
    else:
        preNode.next = None

    return head

if __name__ == "__main__":
    l1 = ListNode(1, ListNode(8))
    l2 = ListNode(0)
    addTwoNumbers(l1, l2)