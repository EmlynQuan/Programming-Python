# coding=UTF-8
import sys

class Solution:
    def judge(self, left, right):
        if right == ')':
            if left == '(':
                return 1
            elif left == '[' or left == '{':
                return -1
            else:
                return 0
        elif right == ']':
            if left == '[':
                return 2
            elif left == '(' or left == '{':
                return -1
            else:
                return 0
        elif right == '}':
            if left == '{':
                return 3
            elif left == '[' or left == '(':
                return -1
            else:
                return 0

    def myStackPop(self, arr, top):
        if len(arr) > 0:
            top -= 1
            return arr.pop(-1), top
        else:
            return


    def myStackPush(self, arr, top, value):
        arr.append(value)
        top += 1
        return top

    def getMatchBracketsNum(self , inString , inStringNum ):
        if len(inString) == 0:
            return -1
        # 栈
        stack = []
        # 栈顶指针
        top = 0

        # 权重
        weight = 0

        # 获取输入
        arr = inString.split(" ")
        # 全部入栈
        for i in range(len(arr)):
            top = self.myStackPush(stack,top, arr[i])

        tempStack = []
        tempTop = 0

        # 如果栈内有数据
        while top > 0:
            # 取栈顶元素
            left, top = self.myStackPop(stack, top)

            # 为空
            if len(tempStack) == 0:
                # 压栈
                tempTop = self.myStackPush(tempStack, tempTop, left)
            # 不为空，需要和栈内元素比较
            else:
                # 取temp栈顶指针
                right, tempTop = self.myStackPop(tempStack, tempTop)
                ret = self.judge(left, right)
                # 不匹配 继续压temp栈
                if ret == 0:
                    tempTop = self.myStackPush(tempStack, tempTop, right)
                    tempTop = self.myStackPush(tempStack, tempTop, left)
                # 如果左遇到的右不匹配直接返回 -1 即可
                elif ret == -1:
                    return -1
                else:
                    weight += ret

        if len(tempStack) > 0:
            return -1
        else:
            return weight

# # 计算粒子的能量
# def cal_energy(arr, length):
#     # 记录对应子序列的能量
#     memo = []
#     for i in range(length):
#         memo.append([0 for _ in range(i+1)])
#     # 记录最大值
#     max = 0
#     for j in range(length-1, 0, -1):
#         # 初始化
#         memo[j][j] = arr[j]
#         max = max if memo[j][j] < max else memo[j][j]
#         print max
#         for i in range(j-1, -1, -1):
#             # 往左边拓展
#             memo[j][i] = -1 * memo[j][i+1] + arr[i]
#             max = max if memo[j][i] < max else memo[j][i]
#             print max
#
#     print(memo)
#     if max < 0:
#         return 0
#     else:
#         return max

# 计算粒子的能量
def cal_energy(arr, length):
    # 记录对应子序列的能量
    memo = 0
    # 记录最大值
    max = 0
    for j in range(length-1, 0, -1):
        # 初始化
        memo = arr[j]
        max = max if memo < max else memo
        for i in range(j-1, -1, -1):
            # 往左边拓展
            memo = -1 * memo + arr[i]
            max = max if memo < max else memo

    if max < 0:
        return 0
    else:
        return max


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 搜索满足条件的日志。 返回值为二维数组，第一维对应待查询时间戳的下标，第二维是命中日志的事件ID
# @param logs long长整型二维数组 日志数据，数组第一维的下标即为事件ID，第二维包含两个long型整数，分别表示起始和结束时间
# @param tss long长整型一维数组 timestamps，表示待查询的多个时间戳
# @return int整型二维数组
#
class Solution:
    def search_log(self , logs , tss ):
        ret = []
        # write code here
        # 遍历带查询的时间戳
        for i in range(len(tss)):
            TS = tss[i]
            temp = []
            # 查找对应于该时间戳的日志ID
            for j in range(len(logs)):
                log = logs[j]
                # 起始时间戳，结束时间戳
                startTS = log[0]
                endTS = log[1]
                # 如果在日志范围内
                if TS <= endTS and TS >= startTS:
                    temp.append(j)
                # elif TS > startTS:
                #     ret.append(temp)
                #     break
        return ret


# 计算是否需要增派兵力
def add_soilder(arrN, arrM):
    counter = 0
    # 分别计算东南西北四个方向的N的最大两值
    up = [0,0,0]
    bottom = [0,0,0]
    left = [0,0,0]
    right = [0,0,0]
    for
    return counter


if __name__ == "__main__":
    # s = Solution()
    # ret = s.getMatchBracketsNum("[ { { } [ ] ) ]", 8)
    # print ret

    # # 读取n
    # n = int(sys.stdin.readline().strip())
    # # 读取每一行
    # line = sys.stdin.readline().strip()
    # # 把每一行的数字分隔后转化成int列表
    # values = list(map(int, line.split()))
    # print(cal_energy(values, n))

    # 读取第一行
    line = sys.stdin.readline().strip()
    nm = list(map(int, line.split()))
    N_loc, M_loc = [],[]
    for i in range(nm[0]):
        # 读取每一行
        line = sys.stdin.readline().strip()
        strList = line.split()
        N_loc.append([int(strList[0]), int(strList[1])])

    for i in range(nm[1]):
        # 读取每一行
        line = sys.stdin.readline().strip()
        strList = line.split()
        M_loc.append([int(strList[0]), int(strList[1])])

    print(add_soilder(N_loc, M_loc))





