# coding=utf-8

def permutation(S):
    """
    :type S: str
    :rtype: List[str]
    """
    length = len(S)
    ret = [""]
    for i in range(length):
        n = len(ret)
        for j in range(n):
            temp = ret[j]
            ret.append(S[i]+temp)
            for pos in range(1,len(temp)+1):
                cur = temp[0:pos] + S[i] + temp[pos:]
                ret.append(cur)
        for j in range(n):
            ret.pop(0)
    return ret

if __name__ == "__main__":
    print permutation("aqc")
