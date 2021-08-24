# _*_ coding = utf-8 _*_
# created by czq on 2021/8/24


# 题目787：
# 有 n 个城市通过一些航班连接。给你一个数组flights ，其中flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格
# pricei 抵达 toi。
#
# 现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k站中转的路线，使得从 src 到 dst 的 价格最便宜 ，
# 并返回该价格。 如果不存在这样的路线，则输出 -1。


# 题解1：
# 思路：用dp[k][j]表示经过k次航班，到达j的最小距离，则dp[k][j] = min(dp[t][j], dp[t-1][i]+cost)，其中i为j的出发城市，cost为i和j的距离，
# dp[0][src] = 0
from math import inf


def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    dp = [[inf] * n for _ in range(k + 2)]
    dp[0][src] = 0
    for t in range(1, k + 2):
        for i, j, cost in flights:
            dp[t][j] = min(dp[t][j], dp[t - 1][i] + cost)
    answer = min(dp[t][dst] for t in range(1, k + 2))
    return answer if answer != inf else -1
