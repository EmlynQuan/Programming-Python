# coding=utf-8

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if len(pushed) == len(popped):
            stack = []
            i = 0
            while i < len(popped):
                print "当前待弹出的元素是：\n"
                print popped[i]
                # 当前弹出的元素
                cur = popped[i]
                # 如果是当前已经压栈的元素
                if len(stack) > 0 and stack[-1] == cur:
                    popped.pop(i)
                    stack.pop(-1)
                # 如果是当前要入栈的元素
                elif len(pushed) > 0 and pushed[0] == cur:
                    popped.pop(i)
                    pushed.pop(0)
                else:
                    pos, flag = 0, False
                    while pos < len(pushed):
                        if pushed[pos] != cur:
                            # 将前面的入栈
                            stack.append(pushed.pop(0))
                        else:
                            pushed.pop(0)
                            flag = True
                            break
                    if flag:
                        # 从popped数组中弹出
                        popped.pop(i)
                    else:
                        return False
            return True

        else:
            return False


if __name__ == "__main__":
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    Solution().validateStackSequences(pushed, popped)