# coding=utf-8

def findMinTime(nodeTimes, graph):
    '''
    :param nodeTimes:[]
    :param graph: [[],[],[],……]
    :return:
    '''
    # 边
    edges = {}
    # 存储入度
    degree = [0 for _ in range(len(nodeTimes))]
    # 结果
    maxTime = 0
    # 构建边和入度
    for i in range(len(nodeTimes)):
        for x in graph[i]:
            if x not in edges.keys():
                edges[x] = [i+1]
            else:
                edges[x].append(i+1)
            degree[i] += 1
    # 队列
    queue = []
    # 将所有入度为 0 的节点放入队列中
    for u in range(len(nodeTimes)):
        if degree[u] == 0:
            queue.append(u+1)

    print edges
    print queue
    # 开始对队列中的所有起点遍历知道耗时上限
    for x in queue:
        maxTime = max(maxTime, getPathSum(edges, x, nodeTimes))
    return maxTime


def getPathSum(edges, key, times):
    # 如果已经到最后
    if key not in edges.keys():
        return times[key-1]
    else:
        maxValue = 0
        for x in edges[key]:
            maxValue = max(maxValue, getPathSum(edges, x, times))
        return maxValue + times[key-1]


if __name__ == '__main__':
    nodes = [3,1,2,5,3,1]
    graph = [[2,3,4],[5],[5,6],[],[6],[]]
    print findMinTime(nodes, graph)