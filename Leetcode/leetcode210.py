# coding=utf-8

# 找到选修课的成绩
def findOrder(numCourses, prerequisites):
    # 边
    edges = {}
    # 存储入度
    degree = [0 for _ in range(numCourses)]
    # 结果
    result = []
    # 构建边和入度
    for temp in prerequisites:
        if temp[1] not in edges.keys():
            edges[temp[1]] = [temp[0]]
        else:
            edges[temp[1]].append(temp[0])
        degree[temp[0]] += 1

    # 队列
    queue = []
    # 将所有入度为 0 的节点放入队列中
    for u in range(numCourses):
        if degree[u] == 0:
            queue.append(u)

    # 如果队列不为空
    while len(queue) > 0:
        # 从队首取出一个节点
        u = queue.pop(0)
        # 放入答案中
        result.append(u)
        if u in edges.keys():
            for v in edges[u]:
                degree[v] -= 1
                # 如果相邻节点 v 的入度为 0，就可以选 v 对应的课程了
                if degree[v] == 0:
                    queue.append(v)

    if len(result) != numCourses:
        result = []
    return result


if __name__ == "__main__":
    print findOrder(4, [[1,0],[2,0],[3,1],[3,2]])


