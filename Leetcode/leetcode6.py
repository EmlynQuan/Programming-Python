# coding=utf-8

def convert(s, numRows):
    if numRows == 1:
        return s
    ret = []
    for i in range(numRows):
        ret.append([])

    gap = 2*numRows-2
    for i in range(len(s)):
        for j in range(numRows, gap):
            if i % gap == j:
                ret[gap-j].append(s[i])
                break
        for j in range(numRows):
            if i % gap == j:
                ret[j].append(s[i])
                break

    ans = ""
    for i in range(numRows):
        ans += "".join(ret[i])

    return ans


if __name__ == "__main__":
    print convert("PAYPALISHIRING", 3)