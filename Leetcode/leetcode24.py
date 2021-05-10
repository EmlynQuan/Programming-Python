# coding=utf-8


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    if head == None:
        return None
    if head.next == None:
        return head

    temp = head
    flag = True
    while temp:
        if flag:
            if temp.next:
                value = temp.val
                temp.val = temp.next.val
                temp.next.val = value
            flag = False
        else:
            flag = True
        temp = temp.next

    return head

