# coding=utf-8

class SortedStack(object):

    def __init__(self):
        self.stack = [None for _ in range(5001)]
        self.count = 0


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.count == 0:
            self.stack[0] = val
        elif self.stack[self.count-1] >= val:
            self.stack[self.count] = val
        else:
            pos = 0
            for i in range(self.count-1, -1, -1):
                if self.stack[i] < val:
                    self.stack[i+1] = self.stack[i]
                else:
                    pos = i+1
                    break
            self.stack[pos] = val

        self.count += 1

    def pop(self):
        """
        :rtype: None
        """
        if self.count > 0:
            self.count -= 1
            return self.stack[self.count]
        else:
            return None


    def peek(self):
        """
        :rtype: int
        """
        if self.count == 0:
            return -1
        else:
            return self.stack[self.count-1]


    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.count == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    myStack = SortedStack()
    myStack.peek()
    myStack.peek()
    myStack.pop()
    myStack.isEmpty()
    myStack.peek()
    myStack.push(40)
    myStack.pop()
    myStack.push(19)
    myStack.peek()
    myStack.push(44)
    myStack.peek()
    myStack.pop()
    myStack.push(42)
    myStack.isEmpty()
    myStack.push(8)
    myStack.peek()
    myStack.isEmpty()
    myStack.push(29)
    myStack.peek()
    myStack.peek()
    myStack.isEmpty()
    myStack.push(25)
    myStack.isEmpty()
    myStack.peek()
    myStack.isEmpty()
    myStack.pop()
    myStack.peek()
    myStack.pop()
    myStack.push(52)
    myStack.push(63)
    myStack.isEmpty()
    myStack.pop()
    myStack.isEmpty()
    myStack.peek()
    myStack.push(47)
    myStack.pop()
    myStack.push(45)
    myStack.push(52)
    myStack.isEmpty()
    myStack.pop()
    myStack.pop()
    myStack.push(17)

'''
 "peek", "isEmpty", "pop", "peek", "push", "push", "peek", "isEmpty",
     "isEmpty", "isEmpty", "isEmpty", "isEmpty", "push", "push", "push", "push", "push", "peek", "peek", "isEmpty",
     "push"]
 [], [], [], [], [6], [30],
     [], [], [], [], [], [], [51], [46], [2], [56], [39], [], [], [], [38]]
'''