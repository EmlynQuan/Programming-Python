# coding=utf-8

class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        while len(stones) > 1:
            left, right = 0, len(stones)-1
            temp = []
            while left < right:
                temp.append(stones[right]-stones[left])
                left += 1
                right -= 1
            if len(stones) % 2 == 1:
                temp.append(stones[left])
            temp.sort()
            stones = temp
        return stones[0]


if __name__ == '__main__':
    s = [31,26,33,21,40]
    print Solution().lastStoneWeightII(s)