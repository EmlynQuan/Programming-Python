# coding=UTF-8
import sys

# ====================================阿里 04.23 笔试1
# 记录一个数组的连续1的最大长度
def getMaxLen(arr):
    # print(arr)
    left, right, maxLen, tempCounter = 0,0,0,0
    # 还可以继续走
    while right < len(arr) and left < len(arr):
        if arr[left] == 0:
            left += 1
            right += 1
        elif arr[right] == 1:
            right += 1
            tempCounter += 1
        else:
            maxLen = tempCounter if tempCounter > maxLen else maxLen
            left = right
    maxLen = tempCounter if tempCounter > maxLen else maxLen
    return maxLen


    return 0

if __name__ == "__main__":
    # 读取第一行的n
    arr = sys.stdin.readline().strip().split()
    n = int(arr[0])
    m = int(arr[1])
    q = int(arr[2])

    matrix = []
    # 读取 n,m 矩阵
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        matrix.append(list(map(int, line.split())))
    op = []
    # 读取 q 行操作
    for i in range(q):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        op.append(list(map(int, line.split())))

    # 备忘录
    memo = [0 for _ in range(n)]
    maxLen = 0
    # 先遍历初始化memo
    for i in range(n):
        memo[i] = getMaxLen(matrix[i])
        maxLen = memo[i] if memo[i] > maxLen else maxLen

    # 遍历操作
    for i in range(q):
        op_i = op[i][0]
        op_j = op[i][1]
        # 翻转格子
        if matrix[op_i-1][op_j-1] == 0:
            matrix[op_i - 1][op_j - 1] = 1
        else:
            matrix[op_i - 1][op_j - 1] = 0

        # 获取当前列表的最大长度
        memo[op_i-1] = getMaxLen(matrix[op_i-1])
        maxLen = 0
        for i in range(n):
            maxLen = memo[i] if memo[i] > maxLen else maxLen
        # print(matrix)
        print(maxLen)



# ====================================阿里 04.23 笔试2

# 对给定的数组和指定下标的几个数据进行移位
def move(arr, idxArr, k):
    temp = []
    for i in range(len(idxArr)):
        temp.append(arr[idxArr[i]])
    # 得到的temp是待移位的数组
    n = len(temp)
    # 循环移动k位
    k = k % n
    # 前k位翻转
    reverse(temp, 0, k-1)
    # 后n-k位翻转
    reverse(temp, k, n-1)
    # 整体翻转
    reverse(temp, 0, n-1)

    i = 0
    # 对应赋值
    for idx in idxArr:
        arr[idx] = temp[i]
        i += 1


# 翻转数组
def reverse(arr, left, right):
    while left < right:
        t = arr[left]
        arr[left] = arr[right]
        arr[right] = t
        left += 1
        right -= 1


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        # 读取每一行
        arr = sys.stdin.readline().strip().split()
        # 节点个数
        n = int(arr[0])
        # 移位数
        k = int(arr[1])
        # 对应的二叉树
        arr = []
        flag = []
        for i in range(n):
            arr.append(i+1)
            flag.append(False)

        for i in range(n):
            # 尚未被加入过集合的节点
            if flag[i] == False:
                # 向集合中添加元素
                tempList = []
                idx = i
                while idx < n:
                    tempList.append(idx)
                    flag[idx] = True
                    # 变成左子节点的下标
                    idx = 2*idx+1
                # 添加完毕后 对每个集合循环移位
                move(arr, tempList, k)

        line = ""
        for i in range(n):
            if i != 0:
                line += ' '
            line += str(arr[i])
        print(line)

