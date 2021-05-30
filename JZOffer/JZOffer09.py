# coding=utf-8

class CQueue(object):

    def __init__(self):
        self.A = []
        self.B = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        while self.A:
            self.B.append(self.A.pop())
        self.A.append(value)


    def deleteHead(self):
        """
        :rtype: int
        """
        while self.B:
            self.A.append(self.B.pop())

        if self.A:
            return self.A.pop()
        else:
            return -1
