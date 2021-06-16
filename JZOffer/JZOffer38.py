# coding=utf-8

class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []

        for i in range(len(s)):
            temp = [x for x in ret]
            for