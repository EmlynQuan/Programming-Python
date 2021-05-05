# coding=utf-8

def permute(nums):
    ret = []
    n = len(nums)
    if n == 0:
        return ret
    else:
        for i in range(n):
            ret.append([nums[i]])

    for i in range(1,n):
        num = len(ret)
        for j in range(num):
            temp = ret[j]
            for value in nums:
                if value not in temp:
                    arr = [v for v in temp]
                    arr.append(value)
                    ret.append(arr)
        # print ret
        for j in range(num-1, -1, -1):
            ret.pop(j)
        # print ret
    return ret


if __name__ == "__main__":
    print permute([1,2,3,5,4])
