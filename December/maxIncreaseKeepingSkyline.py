# _*_ coding = utf-8 _*_
# created by czq on 2021/12/13


# 题目807：
# 给你一座由 n x n 个街区组成的城市，每个街区都包含一座立方体建筑。给你一个下标从 0 开始的 n x n 整数矩阵 grid ，其中 grid[r][c] 表示坐落于 r 行 c 列的建筑物的 高度 。
#
# 城市的 天际线 是从远处观察城市时，所有建筑物形成的外部轮廓。从东、南、西、北四个主要方向观测到的 天际线 可能不同。
#
# 我们被允许为 任意数量的建筑物 的高度增加 任意增量（不同建筑物的增量可能不同） 。 高度为 0 的建筑物的高度也可以增加。然而，增加的建筑物高度 不能影响 从任何主要方向观察城市得到的 天际线 。
#
# 在 不改变 从任何主要方向观测到的城市 天际线 的前提下，返回建筑物可以增加的 最大高度增量总和 。


# 题解1：
# 思路：找出这个位置横竖上最大的值中的最小值，这个就是可以增加的最大高度；
from math import inf


def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
    rows = len(grid)
    cows = len(grid[0])
    cows_ans = []
    res = 0
    for j in range(cows):
        max_cows = -inf
        for i in range(rows):
            max_cows = max(max_cows, grid[i][j])
        cows_ans.append(max_cows)
    for i in range(rows):
        for j in range(cows):
            res += min(max(grid[i]), cows_ans[j]) - grid[i][j]
    return res
