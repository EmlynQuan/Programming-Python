# coding=utf-8
from collections import defaultdict

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        myDict = defaultdict(set)
        newHead = Node(0)
        newcur, cur = newHead, head
        while cur:
            newcur.next = Node(cur.val)
            if cur.random:
                myDict[cur.random].add(newcur.next)
            cur = cur.next
            newcur = newcur.next

        newcur, cur = newHead, head
        while cur:
            if cur in myDict.keys():
                for x in myDict[cur]:
                    x.random = newcur.next
            cur = cur.next
            newcur = newcur.next

        return newHead.next


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n1.next, n1.random = n2, n2
    n2.random = n2

    Solution().copyRandomList(n1)