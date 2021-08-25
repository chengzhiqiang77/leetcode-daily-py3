# _*_ coding = utf-8 _*_
# created by czq on 2021/8/25


# 题目797：
# 给你一个有n个节点的 有向无环图（DAG），请你找出所有从节点 0到节点 n-1的路径并输出（不要求按特定顺序）
#
# 二维数组的第 i 个数组中的单元都表示有向图中 i 号节点所能到达的下一些节点，空就是没有下一个结点了。


# 题解1：
# 思路：使用DFS，用一个栈来记录从0出发可以到达的所有路径，当路径满足条件，则把该路径加入到答案中，然后出栈，继续进行搜索


def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
    route = []
    answer = []

    def dfs(x: int):
        if x == len(graph) - 1:
            answer.append(route[:])
            return

        if x == 0:
            route.append(0)

        for y in graph[x]:
            route.append(y)
            dfs(y)
            route.pop()

    dfs(0)
    return answer
