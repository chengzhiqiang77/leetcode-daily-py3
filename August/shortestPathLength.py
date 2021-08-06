# _*_ coding = utf-8 _*_
# created by czq on 2021/8/6


# 题目847：
# 存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。
#
# 给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。
#
# 返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。


# 题解1：（今天没有任何思路，昨天熬夜项目上线，脑子不清晰了，今天的思路和代码来源于leetcode大佬@Benhao）
# 思路：这题目可以用多源BFS做，从每一个的点出发，最终的目标是走过所有的点


def shortestPathLength(self, graph: List[List[int]]) -> int:
    n = len(graph)
    # 初始以每个点为起点
    frontier = [(i, 1 << i) for i in range(n)]
    explored = set(frontier)
    # 目标为2^n - 1
    goal = (1 << n) - 1
    step = 0
    while frontier:
        nxt = []
        for cur, state in frontier:
            if state == goal:
                return step
            for other in graph[cur]:
                # 下一个状态
                successor = (other, 1 << other | state)
                # 新的状态没有被走过
                if successor not in explored:
                    explored.add(successor)
                    nxt.append(successor)
        frontier = nxt
        step += 1
    # 图不连通
    return -1
