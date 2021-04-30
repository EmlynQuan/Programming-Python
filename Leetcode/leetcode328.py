# coding=utf-8

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    if head == None:
        return head
    oddHead = head
    oddTail = head
    if head.next:
        EvenHead = head.next
        EvenTail = head.next
    else:
        return head

    counter = 1

    head = head.next
    while head.next:
        if counter % 2 == 1:
            oddTail.next = head.next
            oddTail = oddTail.next
        else:
            EvenTail.next = head.next
            EvenTail = EvenTail.next
        counter += 1
        head = head.next

    oddTail.next = EvenHead
    EvenTail.next = None
    return oddHead

if __name__ == "__main__":
    n4 = ListNode(5, None)
    n3 = ListNode(4, n4)
    n2 = ListNode(3, n3)
    n1 = ListNode(2, n2)
    head = ListNode(1,n1)

    head = oddEvenList(head)

    while head:
        print head.val
        head = head.next

