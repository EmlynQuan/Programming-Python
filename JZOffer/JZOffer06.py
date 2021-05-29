# coding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reversePrint(head):
    if head == None:
        return []
    ret = []
    while head:
        ret.append(head.val)
        head = head.next

    i,j = 0, len(ret)-1
    while i < j:
        temp = ret[i]
        ret[i] = ret[j]
        ret[j] = temp
        i += 1
        j -= 1

    return ret
