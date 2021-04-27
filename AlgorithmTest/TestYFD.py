#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

# 判断当前序列是否整体为非递增序
def judgeArr(arr):
    if len(arr) < 2:
        return True, arr[0], arr[0]
    for i in range(0, len(arr)-1):
        if arr[i] < arr[i+1]:
            return False,None,None
    return True,arr[0], arr[-1]

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))[1:]
        # print(values)

        if len(values) < 2:
            print('Y')
        else:
            allflag,_,_ = judgeArr(values)
            if allflag:
                print('Y')
            else:
                flag = False
                for pos in range(1, len(values)):
                    # print(values[0:pos])
                    # print(values[pos:len(values)])
                    preF, preMax, preMin = judgeArr(values[0:pos])
                    if preF:
                        aftF, aftMax, aftMin = judgeArr(values[pos:len(values)])
                        if aftF:
                            if preMax <= aftMin:
                                flag = True
                                print('Y')
                                break

                if flag == False:
                    print('N')


'''
def findNum(arr, num):
    counter = 0
    for i in range(0, len(arr)):
        if arr[i] <= num:
            counter += 1
    return counter
    
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    # print(values)
    line = sys.stdin.readline().strip().split()
    target = int(line[0])
    counter = findNum(values, target)
    print(counter)
    
'''



'''
def getSum(arr, adj):
    counter = 0
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if adj[i][j] == 1:
                temp = arr[i] | arr[j]
                counter += temp
    return counter

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(T):
        # N
        N = int(sys.stdin.readline().strip())
        # arr
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))

        # adj
        adj = []
        for t in range(0, N):
            adj.append([0 for _ in range(N)])
        # u , v
        for j in range(N-1):
            temp = list(map(int, sys.stdin.readline().strip().split()))
            adj[temp[0]-1][temp[1]-1] = 1
        for j in range(N):
            adj[j][j] = 1
        print(getSum(values, adj))
'''