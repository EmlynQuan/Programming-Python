# coding=utf-8

def grayCode(n):
    ans = [0]
    if n == 0:
        return ans
    else:
        head = 1
        for i in range(n):
            for j in range(len(ans)-1, -1, -1):
                ans.append(head+ans[j])
            head <<= 1
    return ans

if __name__ == "__main__":
    test = 4
    print grayCode(test)