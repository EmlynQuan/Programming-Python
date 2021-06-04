# coding=utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        myDict = {}
        maxValue, start, curLen = 0, 0, 0
        for i in range(len(s)):
            if s[i] in myDict.keys():
                pre = myDict[s[i]]
                maxValue = max(maxValue, curLen)
                if pre > start:
                    curLen = i - pre
                    start = pre + 1
                else:
                    curLen = i - start
                for key in myDict.keys():
                    if myDict[key] < start:
                        del myDict[key]
                myDict[s[i]] = i
            else:
                myDict[s[i]] = i
                curLen += 1
        maxValue = max(maxValue, curLen)
        return maxValue


if __name__ == '__main__':
    Solution().lengthOfLongestSubstring("tmmzuxt")