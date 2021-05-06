class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle1(head):
    '''
    可以AC
    :param head:
    :return:
    '''
    slowCounter, fastCounter = 1, 1
    flag = False
    fast, slow = head, head

    # 快慢指针
    while slow and fast:
        slow = slow.next
        slowCounter += 1
        if slow == None:
            break
        else:
            fast = fast.next
            if fast:
                fast = fast.next
                fastCounter += 2
            else:
                break
            if slow == fast:
                flag = True
                break

    # 环的长度 fastCounter = 2*slowCounter
    pos = fastCounter-slowCounter

    # 存在环
    if flag:
        while head:
            slow = head
            for i in range(pos):
                slow = slow.next

            if slow == head:
                return slow

            head = head.next
    else:
        return None


def detectCycle(head):
    '''
    优化版本
    '''
    slowCounter = 1
    flag = False
    fast, slow, curP = head, head, head

    # 快慢指针
    while slow and fast:
        slow = slow.next
        slowCounter += 1
        if slow == None:
            break
        else:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break
            if slow == fast:
                flag = True
                break

    if flag:
        while curP != slow:
            curP = curP.next
            slow = slow.next
        return slow
    else:
        return None



