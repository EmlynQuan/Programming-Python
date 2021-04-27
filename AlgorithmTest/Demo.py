# coding=UTF-8

# 1。 字符串反转
def reverseStr(input):
    if len(input) == 0:
        return input
    string = list(input)
    # 定义两个指针 begin和end
    begin = 0
    end = len(input)-1
    # 如果begin指针小于end指针
    while begin < end:
        temp = string[begin]
        string[begin] = string[end]
        string[end] = temp
        # 指针移动
        begin = begin + 1
        end = end - 1
    return ''.join(string)

# 2。 链表类的定义
class Node():
    def __init__(self, value, next):
        self.node = value
        self._next = next

    def __str__(self):
        return str(self.node)

class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return (self.length == 0)

    def addNodeAfter(self, value):
        if self.length == 0:
            self.head = Node(value, None)
        else:
            p = self.head
            while p._next:
                p = p._next
            p._next = Node(value, None)

        self.length += 1

    def addNodeBefore(self, value):
        if self.length == 0:
            self.head = Node(value, None)
        else:
            p = self.head
            Head = Node(value, p)
            self.head = Head

        self.length += 1

    def __str__(self):
        ret = ""
        if self.length == 0:
            return None
        else:
            p = self.head
            while p:
                ret += str(p)
                p = p._next
        return ret

# 2。 链表反转
def reverseLinkedList(input):
    if input.length <= 1:
        return input

    p = input.head
    NewHead = LinkedList()
    NewHead.addNodeAfter(p.node)

    while p._next:
        p = p._next
        NewHead.addNodeBefore(p.node)

    return str(NewHead)

# 3。 有序数组合并
def mergeList(list1, list2):
    ret = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] > list2[0]:
            ret.append(list2[0])
            list2 = list2[1:]
        else:
            ret.append(list1[0])
            list1 = list1[1:]

    if len(list1) != 0:
        ret.extend(list1)
    else:
        ret.extend(list2)

    return ret


# 4。 Hash 算法 (在一个字符串中找到第一个只出现一次的字符)
def findFirstChar_Hash(input):
    counter = [0 for _ in range(0,26)]
    stringList = list(input)
    for x in stringList:
        index = ord(x)-ord('a')
        counter[index] += 1
    for x in stringList:
        index = ord(x)-ord('a')
        if counter[index] == 1:
            return x

# 5。 求无序数组中的中位数
# 方法1：排序算法 + 中位数
# 方法2：利用快排思想（分治思想）
def getMidNum(input):
    left = 0
    right = len(input)-1
    anchor = input[right]


# 硬币兑换 给定一个硬币数组和一个需要兑换的值，求解兑换该金额最少的硬币数
# 默认每种硬币数没有上限
# 记忆化搜索
def coinChange(coins, amount):
    if len(coins) == 0:
        return -1
    else:
        memo = [0 for _ in range(amount)]
        return findWay(coins, amount, memo)

# 搜索可能的解, 返回值为硬币数
def findWay(arr, amount, memo):
    if amount < 0:
        return -1
    elif amount == 0:
        return 0
    # amount数值的硬币数已经计算过 所以直接读取备忘录内容即可
    elif memo[amount-1] != 0:
        return memo[amount-1]
    else:
        min = amount+1
        # 遍历可能的硬币组合
        for i in range(len(arr)):
            result = findWay(arr, amount-arr[i], memo)
            # 是可以兑换的 且是满足更小的
            if result >= 0 and result < min:
                # 更新最小值
                min = result + 1

        # 是更新过的值
        if min < amount+1:
            memo[amount-1] = min
        # 当前amount无解
        else:
            memo[amount-1] = -1
        return memo[amount-1]


# 接雨水: 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
def trap(height):
    if len(height) <= 2:
        return 0

    size = len(height)
    # 雨水总和
    sum = 0
    # 最大左边 和 最大右边
    maxLeft = [0 for _ in range(size)]
    maxRight = [0 for _ in range(size)]
    maxLeft[0] = height[0]
    maxRight[size-1] = height[size-1]
    # maxLeft
    for i in range(1,size):
        maxLeft[i] = max(height[i],maxLeft[i-1])
    # maxRight
    for i in range(size-2, -1, -1):
        # 更新
        maxRight[i] = max(height[i], maxRight[i+1])
        # 求和
        sum += min(maxRight[i], maxLeft[i]) - height[i]

    # print maxLeft
    # print maxRight
    return sum


# 接雨水 优化 双指针
def trap2(height):
    if len(height) <= 2:
        return 0
    max_left, max_right = 0,0
    sum = 0
    left = 0
    right = len(height)-1

    while left < right:
        # 左边的可以判断加
        if height[left] < height[right]:
            max_left = max(max_left, height[left])
            sum += max_left - height[left]
            left += 1
        else:
            max_right = max(max_right, height[right])
            sum += max_right - height[right]
            right -= 1

    return sum

# 最短的桥
# 在给定的二维二进制数组中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）现在，我们可以将0变为1，以使两座岛连接起来，变成一座岛。
# 返回必须翻转的0 的最小数目。（可以保证答案至少是 1 。）
# 通过dfs去搜索一个岛，然后通过bfs去搜索如何连通第二个岛，找到第二个岛的层数就是需要翻转的0，1数
def bridge(grid):
    if len(grid) == 0:
        return 0

    points = []
    flag = False
    first = []
    m,n = len(grid),len(grid[0])
    # 找第一个岛
    for i in range(m):
        if flag == True:
            break
        for j in range(n):
            # 找到某个岛的第一个点
            if grid[i][j] == 1:
                first.append(i)
                first.append(j)
                first.append(0)
                points.append(first)
                # 修改其为2 用于区分岛1和岛2
                grid[i][j] = 2
                flag = True
                break

    dfs_grid(grid, m, n, points, first)
    print points

    # 进行广度优先搜索 判断需要几层才能找到另一座岛
    return bfs_grid(grid, points, m, n)


# 深度优先搜索 搜索完整的一个岛
def dfs_grid(grid, m, n, pointArray, curPoint):
    i = curPoint[0]
    j = curPoint[1]

    # 上下左右
    pos_i = [-1,1,0,0]
    pos_j = [0,0,-1,1]
    # 遍历四个方向
    for loop in range(4):
        if i+pos_i[loop] >= 0 and i+pos_i[loop] < m and j+pos_j[loop] >= 0 and j+pos_j[loop] < n:
            if grid[i+pos_i[loop]][j+pos_j[loop]] == 1:
                grid[i+pos_i[loop]][j+pos_j[loop]] = 2
                temp = [i+pos_i[loop],j+pos_j[loop],0]
                pointArray.append(temp)
                dfs_grid(grid,m,n,pointArray,temp)


# 广度优先搜索 找到另一座岛
def bfs_grid(grid, points, m, n):
    # 直到队列为空
    while len(points) > 0:
        firstPoint = points[0]
        i = firstPoint[0]
        j = firstPoint[1]
        level = firstPoint[2]

        # 上下左右
        pos_i = [-1, 1, 0, 0]
        pos_j = [0, 0, -1, 1]
        # 遍历四个方向
        for loop in range(4):
            if i + pos_i[loop] >= 0 and i + pos_i[loop] < m and j + pos_j[loop] >= 0 and j + pos_j[loop] < n:
                if grid[i + pos_i[loop]][j + pos_j[loop]] == 0:
                    grid[i + pos_i[loop]][j + pos_j[loop]] = 2
                    temp = [i + pos_i[loop], j + pos_j[loop], level + 1]
                    points.append(temp)
                elif grid[i + pos_i[loop]][j + pos_j[loop]] == 1:
                    return level

        points.pop(0)



# 四则运算
def pop(arr):
    if len(arr) > 0:
        ret = arr[len(arr)-1]
        del arr[-1]
        return ret
    else:
        return None

def push(arr, value):
    arr.append(value)
    return

def tool(left, right, op):
    ret = 0
    if op == '+':
        ret = left + right
    elif op == '-':
        ret = left - right
    elif op == '*':
        ret = left * right
    elif op == '/':
        ret = left / right
    return ret

# 计算
def cal(arrNum, arrOp):
    ret = 0
    op = pop(arrOp)
    while op != None:
        opNext = pop(arrOp)
        if opNext == None:
            right = pop(arrNum)
            left = pop(arrNum)
            ret = tool(left, right, op)
        # 只有这一种情况先算后面的
        elif (op == '*' or op == '/') and (opNext == '+' or opNext == '-'):
            right = pop(arrNum)
            left = pop(arrNum)
            ret = tool(left, right, op)
            push(arrNum, ret)
            push(arrOp, opNext)
        else:
            temp = pop(arrNum)
            right = pop(arrNum)
            left = pop(arrNum)
            push(arrOp, op)
            ret = tool(left, right, opNext)
            push(arrNum,ret)
            push(arrNum, temp)

        op = pop(arrOp)

    return ret


# 主函数
if __name__ == "__main__":
    '''
    单链表反转
    NewHead = LinkedList()
    NewHead.addNodeAfter("1")
    NewHead.addNodeAfter("2")
    NewHead.addNodeAfter("3")
    NewHead.addNodeAfter("4")
    print NewHead
    print reverseLinkedList(NewHead)
    '''

    '''
    有序数组合并
    l1 = [1,2,3,7,8,9,12,19]
    l2 = [4,5,6,10,14]
    print mergeList(l1,l2)
    '''

    '''哈希映射解决查找字符串中第一个出现过一次的字符
    test = "avvfjrfraqdkwqd"
    print findFirstChar_Hash(test)
    '''

    '''
    # 接雨水
    arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    print trap(arr)
    print trap2(arr)
    '''

    '''
    grid = [[0,1,0],[0,0,0],[0,0,1]]
    print '翻转次数：\n'
    print bridge(grid)
    '''

    '''
    # 四则运算
    arrNum = [12,6,3,41]
    arrOp = ['-','/','+']
    print cal(arrNum, arrOp)
    '''

    print('over')


