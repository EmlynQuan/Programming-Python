# coding=utf-8

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    '''
    对链表排序
    '''
    return helpSort(head, None)


def helpSort(head, tail):
    # 头为空
    if not head:
        return head
    # 只有一个节点
    if head.next == tail:
        head.next = None
        return head
    # 超过两个节点
    slow = fast = head
    while fast != tail:
        slow = slow.next
        fast = fast.next
        if fast != tail:
            fast = fast.next
    mid = slow
    return merge(helpSort(head, mid), helpSort(mid, tail))


def merge(head1, head2):
    ret = ListNode(0)
    pos = ret
    temp1, temp2 = head1, head2
    while temp1 and temp2:
        if temp1.val < temp2.val:
            pos.next = head1
            temp1 = temp1.next
        else:
            pos.next = temp2
            temp2 = temp2.next
        pos = pos.next
    if temp1:
        pos.next = temp1
    if temp2:
        pos.next = temp2
    return ret.next