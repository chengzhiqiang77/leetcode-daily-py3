# _*_ coding = utf-8 _*_
# created by czq on 2021/11/12


# 题目488：
# 你正在参与祖玛游戏的一个变种。
#
# 在这个祖玛游戏变体中，桌面上有 一排 彩球，每个球的颜色可能是：红色 'R'、黄色 'Y'、蓝色 'B'、绿色 'G' 或白色 'W' 。你的手中也有一些彩球。
#
# 你的目标是 清空 桌面上所有的球。每一回合：
#
# 从你手上的彩球中选出 任意一颗 ，然后将其插入桌面上那一排球中：两球之间或这一排球的任一端。
# 接着，如果有出现 三个或者三个以上 且 颜色相同 的球相连的话，就把它们移除掉。
# 如果这种移除操作同样导致出现三个或者三个以上且颜色相同的球相连，则可以继续移除这些球，直到不再满足移除条件。
# 如果桌面上所有球都被移除，则认为你赢得本场游戏。
# 重复这个过程，直到你赢了游戏或者手中没有更多的球。
# 给你一个字符串 board ，表示桌面上最开始的那排球。另给你一个字符串 hand ，表示手里的彩球。请你按上述操作步骤移除掉桌上所有球，计算并返回所需的 最少 球数。如果不能移除桌上所有的球，返回 -1 。


# 题解1：
# 思路：枚举所有的情况，计算出最优情况
from collections import Counter
from functools import lru_cache
from math import inf


def findMinStep(self, board: str, hand: str) -> int:
    COLORS = ["R", "Y", "B", "G", "W"]
    cnts, cnts_b = Counter(hand), Counter(board)
    total = len(hand)
    if any(cnts_b[k] + cnts[k] < 3 for k in cnts_b.keys()):
        return -1

    @lru_cache(None)
    def dfs(bd, hd):
        n = len(bd)
        if n <= 0:
            return total - sum(hd)
        ans = inf
        for i, v in enumerate(hd):
            if v:
                cp = list(hd)
                cp[i] -= 1
                nt = tuple(cp)
                # 枚举插入位置
                for j in range(n + 1):
                    ans = min(ans, dfs(in_a_row(bd[:j] + COLORS[i] + bd[j:]), nt))
        return ans

    # 移除相同小球方法
    @lru_cache(None)
    def in_a_row(bd):
        l = r = 0
        while l < len(bd):
            while r < len(bd) and bd[r] == bd[l]:
                r += 1
            if r - l > 2:
                return in_a_row(bd[:l] + bd[r:])
            l = r
        return bd

    start = [cnts[c] for c in COLORS]
    res = dfs(board, tuple(start))
    return res if res != inf else -1
