# coding=utf-8

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    if head.next == None:
        return None

    preNode, curNode, nextNode = head, head, head
    counter = 0
    flag = False

    pos = head
    while pos:
        counter += 1
        if counter == n:
            flag = True
            nextNode = curNode.next
        if flag:
            if counter != n+1:
                preNode = preNode.next
            curNode = curNode.next
            nextNode = nextNode.next
        pos = pos.next

    print curNode.val
    if curNode == head:
        head = head.next
    else:
        preNode.next = nextNode
    return head

