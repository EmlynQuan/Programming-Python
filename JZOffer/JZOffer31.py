# coding=utf-8

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if len(pushed) == len(popped):
            n = len(popped)
            stack = []
            i = 0
            while i < n:
                # 当前弹出的元素
                cur = popped[i]
                pos = 0
                while pos < len(pushed):
                    if pushed[pos] != cur:
                        # 将前面的入栈
                        stack.append(pushed.pop(0))
                    else:
                        pushed.pop(0)
                        break
        else:
            return False