# _*_ coding = utf-8 _*_
# created by czq on 2021/11/4


# 题目407：
# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。


# 题解1：
# 思路：不会做555
import heapq


def trapRainWater(self, heightMap: list[list[int]]) -> int:
    if len(heightMap) <= 2 or len(heightMap[0]) <= 2:
        return 0

    m, n = len(heightMap), len(heightMap[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    pq = []
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                visited[i][j] = 1
                heapq.heappush(pq, (heightMap[i][j], i * n + j))

    res = 0
    dirs = [-1, 0, 1, 0, -1]
    while pq:
        height, position = heapq.heappop(pq)
        for k in range(4):
            nx, ny = position // n + dirs[k], position % n + dirs[k + 1]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0:
                if height > heightMap[nx][ny]:
                    res += height - heightMap[nx][ny]
                visited[nx][ny] = 1
                heapq.heappush(pq, (max(height, heightMap[nx][ny]), nx * n + ny))
    return res
