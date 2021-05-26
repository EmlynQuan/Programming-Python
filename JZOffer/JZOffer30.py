# coding=utf-8

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []     # 数据栈
        self.B = []     # 辅助栈

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)


    def pop(self):
        """
        :rtype: None
        """
        if self.A:
            temp = self.A.pop(-1)
            if temp == self.B[-1]:
                self.B.pop(-1)
            return temp
        else:
            return None


    def top(self):
        """
        :rtype: int
        """
        if self.A:
            return self.A[-1]
        else:
            return None


    def min(self):
        """
        :rtype: int
        """
        if self.B:
            return self.B[-1]
        else:
            return None
