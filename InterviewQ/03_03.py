# coding=utf-8

class StackOfPlates(object):

    def __init__(self, cap):
        """
        :type cap: int
        """
        self.stacks = []
        self.cap = cap

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.cap <= 0:
            return
        if len(self.stacks) == 0:
            self.stacks.append([])
        if len(self.stacks[-1]) < self.cap:
            self.stacks[-1].append(val)
        else:
            self.stacks.append([val])


    def pop(self):
        """
        :rtype: int
        """
        if len(self.stacks) == 0:
            return -1
        else:
            temp = self.stacks[-1].pop(-1)
            if len(self.stacks[-1]) == 0:
                self.stacks.pop(-1)
            return temp

    def popAt(self, index):
        """
        :type index: int
        :rtype: int
        """
        # 不存在指定栈
        if len(self.stacks) < index+1:
            return -1
        # 指定栈删除
        else:
            temp = self.stacks[index].pop(-1)
            if len(self.stacks[index]) == 0:
                self.stacks.pop(index)
            return temp
