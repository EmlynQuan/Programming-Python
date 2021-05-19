# coding=utf-8
import collections
def countPoints(points, queries):
    """
    :type points: List[List[int]]
    :type queries: List[List[int]]
    :rtype: List[int]
    """

    strList = []
    for p in points:
        strList.append(str(p[0]) + "," + str(p[1]))

    # 构建字典
    myDict = collections.Counter(strList)
    ret = []
    x,y,r,ans = 0,0,0,0
    # 遍历查询
    for query in queries:
        ans = 0
        x, y, r = query[0], query[1], query[2]
        # 遍历字典
        for key in myDict.keys():
            temp = key.split(',')
            if (x - int(temp[0])) ** 2 + (y - int(temp[1])) ** 2 <= r ** 2:
                ans += myDict[key]
        ret.append(ans)

    return ret