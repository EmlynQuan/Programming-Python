# coding=utf-8

def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ret = [[]]
    # 遍历每个元素
    for num in nums:
        length = len(ret)
        for i in range(length):
            cur = [x for x in ret[i]]
            cur.append(num)
            ret.append(cur)
    return ret


if __name__ == "__main__":
    print subsets([1,2,3])
