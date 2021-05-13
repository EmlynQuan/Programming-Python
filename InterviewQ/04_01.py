# coding=utf-8
from collections import defaultdict

def findWhetherExistsPath(n, graph, start, target):
    """
    :type n: int
    :type graph: List[List[int]]
    :type start: int
    :type target: int
    :rtype: bool
    """
    hashMap = defaultdict(set)
    # 用字典来构建邻接表
    for key, value in graph:
        hashMap[value].add(key)

    # 标记是否访问
    visited = [False for _ in range(n)]
    return dfs(hashMap, visited, target, start)

# 搜索
def dfs(edges, visited, curNode, target):
    if curNode == target:
        return True
    if visited[curNode]:
        return False

    visited[curNode] = True
    if curNode in edges.keys():
        for end in edges[curNode]:
            if dfs(edges, visited, end, target):
                return True
    return False

if __name__ == "__main__":
    n = 4
    graph = [[0, 1], [0, 2], [1, 0], [1, 3]]
    start = 0
    target = 3
    # 倒序解决 从末尾开始找
    print findWhetherExistsPath(n, graph,start, target)
