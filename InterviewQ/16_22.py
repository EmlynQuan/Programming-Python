# coding=utf-8

def printKMoves(K):
    """
    :type K: int
    :rtype: List[str]
    """
    # 初始化
    black, white = 'X', '_'
    direction = ['R', 'D', 'L', 'U']
    dp = [['R']]
    dirIdx, dirVarValue = 0, 1
    dirVarI = [0,1,0,-1]
    dirVarJ = [1,0,-1,0]
    curI, curJ, curValue, tempI, tempJ = 0, 0, white, 0, 0
    while K > 0:
        # 当前是黑色
        if curValue == black:
            dirVarValue = -1
            dirIdx = (dirIdx + dirVarValue) % 4
            dp[curI][curJ] = white
        # 当前网格是白色
        elif curValue == white:
            dirVarValue = 1
            dirIdx = (dirIdx + dirVarValue) % 4
            dp[curI][curJ] = black


        tempI, tempJ = curI + dirVarI[dirIdx], curJ + dirVarJ[dirIdx]
        n = len(dp)
        m = len(dp[0])

        # 需要开辟新的空间
        if tempI < 0:
            temp = ['_' for _ in range(m)]
            dp.insert(0, temp)
            tempI = 0
        elif tempI >= n:
            temp = ['_' for _ in range(m)]
            dp.append(temp)

        if tempJ < 0:
            for i in range(n):
                dp[i].insert(0,'_')
                tempJ = 0
        elif tempJ >= m:
            for i in range(n):
                dp[i].append('_')

        # 修改网格
        curValue = dp[tempI][tempJ]
        dp[tempI][tempJ] = direction[dirIdx]

        curI, curJ = tempI, tempJ
        K -= 1

    ret = []
    for i in range(len(dp)):
        ret.append("".join(dp[i]))
    return ret



if __name__ == "__main__":
    print printKMoves(K=6)