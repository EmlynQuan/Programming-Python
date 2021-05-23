# coding=utf-8

class Trie():
    L = 30
    def __init__(self):
        self.left = None
        self.right = None
        self.min_value = float("inf")

    def insert(self, val):
        cur = self
        cur.min_value = min(cur.min_value, val)
        for i in range(Trie.L, -1, -1):
            bit = (val >> i) & 1
            if bit == 0:
                if not cur.left:
                    cur.left = Trie()
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = Trie()
                cur = cur.right
            cur.min_value = min(cur.min_value, val)

    def getMaxXorWithLimit(self, val, limit):
        cur = self
        if cur.min_value > limit:
            return -1

        ans = 0
        for i in range(Trie.L, -1, -1):
            bit = (val >> i) & 1
            check = False
            if bit == 0:
                if cur.right and cur.right.min_value <= limit:
                    cur = cur.right
                    check = True
                else:
                    cur = cur.left
            else:
                if cur.left and cur.left.min_value <= limit:
                    cur = cur.left
                    check = True
                else:
                    cur = cur.right
            if check:
                ans |= 1 << i
        return ans

def maximizeXor(nums, queries):
    """
    :type nums: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    root = Trie()
    # 遍历数组建立数 0-left 1-right
    for val in nums:
        root.insert(val)
    # 遍历查询
    ans = [0] * len(queries)
    for i, (x, m) in enumerate(queries):
        ans[i] = root.getMaxXorWithLimit(x, m)
    return ans


if __name__ == "__main__":
    nums = [536870912,0,534710168,330218644,142254206]
    queries = [[214004,404207941]]
    print maximizeXor(nums, queries)

    queries = sorted([(x, m, i) for i, (x, m) in enumerate(queries)], key=lambda query: query[1])
