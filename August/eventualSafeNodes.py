# _*_ coding = utf-8 _*_
# created by czq on 2021/8/5


# 题目802：
# 在有向图中，以某个节点为起始节点，从该点出发，每一步沿着图中的一条有向边行走。如果到达的节点是终点（即它没有连出的有向边），则停止。
#
# 对于一个起始节点，如果从该节点出发，无论每一步选择沿哪条有向边行走，最后必然在有限步内到达终点，则将该起始节点称作是 安全 的。
#
# 返回一个由图中所有安全的起始节点组成的数组作为答案。答案数组中的元素应当按 升序 排列。
#
# 该有向图有 n 个节点，按 0 到 n - 1 编号，其中 n 是graph的节点数。图以下述形式给出：graph[i] 是编号 j 节点的一个列表，满足 (i, j)
# 是图的一条有向边。


# 题解1：
# 思路：我们定义节点的出度为该节点能到达下个节点的路径长度，如果节点到达的点为终点（终点的定义为出度为0的点），
# 则该节点的出度减1，最后只需要输出所有出度为0的节点即可，输出的同时需要保持顺序；
from collections import deque


def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
    n = len(graph)
    visited = [False] * n  # 记录是否节点的出度为0，并保持顺序
    out = [0] * n  # 记录节点的出度
    reverse = [[] for _ in range(n)]  # 构建邻接矩阵保存所能到达节点的个数
    for i in range(n):
        out[i] = len(graph[i])
        for j in graph[i]:
            reverse[j].append(i)
    result = deque()
    answer = []
    for i in range(n):
        if len(graph[i]) == 0:
            result.append(i)
    while result:
        cur = result.popleft()
        visited[cur] = True
        for j in reverse[cur]:
            out[j] -= 1
            if out[j] == 0:
                result.append(j)
    for i in range(n):
        if visited[i]:
            answer.append(i)
    return answer
