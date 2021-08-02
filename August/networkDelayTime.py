# _*_ coding = utf-8 _*_
# created by czq on 2021/8/2


# 题目743：
# 有 n 个网络节点，标记为1到 n。
#
# 给你一个列表times，表示信号经过 有向 边的传递时间。times[i] = (ui, vi, wi)，其中ui是源节点，vi是目标节点，
# wi是一个信号从源节点传递到目标节点的时间。
#
# 现在，从某个节点K发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回-1 。


# 题解1：
# 思路：这道题可以转换为从k到各个点的距离的最小长度，我们可以使用Dijkstra算法求解
import collections
import heapq


def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
    # 根据times构建邻接矩阵
    dist = [[float('inf')] * n for i in range(n)]
    dic_adj = collections.defaultdict(list)
    for u, v, w in times:
        dist[u - 1][v - 1] = w
        dic_adj[u - 1].append(v - 1)

    # que=[[距离,点]]用于保存更新后k到其他点的距离 visited保存已经确定最小距离的{点:距离}
    que = [(0, k - 1)]
    visited = {}
    while que:
        dist_pos, pos = heapq.heappop(que)
        # 如果pos的最短距离早已确定 直接跳过 这句很重要！！！
        if pos in visited:
            continue
        # 否则 添加已确定距离 如果n个都确定则停止循环
        visited[pos] = dist_pos
        if len(visited) == n:
            break
        # 根据历经pos的情况 更新从k-1到pos的邻接点的最小距离
        for v in dic_adj[pos]:
            if v not in visited:
                dist[k - 1][v] = min(dist[k - 1][v], dist[k - 1][pos] + dist[pos][v])
                heapq.heappush(que, (dist[k - 1][v], v))
    return max(visited.values()) if len(visited) == n else -1
