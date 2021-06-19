# coding=utf-8

class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = [s[0]]
        # 第i个位置的字符
        for i in range(1,len(s)):
            # 获取当前已经得到的集合
            temp = [x for x in ret]
            length = len(temp[0])+1
            ret = []
            # 遍历所有已经存在的字符集合
            for j in range(len(temp)):
                # 遍历每个位置
                for pos in range(length):
                    curStr = temp[j][:pos]+s[i]+temp[j][pos:]
                    if curStr not in ret:
                        ret.append(curStr)

        return ret

