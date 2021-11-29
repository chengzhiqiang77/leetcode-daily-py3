# _*_ coding = utf-8 _*_
# created by czq on 2021/11/29


# 题目519：
# 给你一个 m x n 的二元矩阵 matrix ，且所有值被初始化为 0 。请你设计一个算法，随机选取一个满足matrix[i][j] == 0 的下标(i, j)
# ，并将它的值变为 1 。所有满足 matrix[i][j] == 0 的下标 (i, j) 被选取的概率应当均等。
#
# 尽量最少调用内置的随机函数，并且优化时间和空间复杂度。
#
# 实现 Solution 类：
#
# Solution(int m, int n) 使用二元矩阵的大小 m 和 n 初始化该对象
# int[] flip() 返回一个满足matrix[i][j] == 0 的随机下标 [i, j] ，并将其对应格子中的值变为 1
# void reset() 将矩阵中所有的值重置为 0


# 题解1：
# 思路：用一个一维数组来代表这个二元矩阵，用一个字典来代表翻转的矩阵，将翻转的索引位置与最后一位交换，然后随机的数字减少一位，这样就实现了随机翻转的功能
import random


class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.map = {}

    def flip(self):
        x = random.randint(0, self.total-1)
        self.total -= 1
        # 查找位置 x 对应的映射
        idx = self.map.get(x, x)
        # 将位置 x 对应的映射设置为位置 total 对应的映射
        self.map[x] = self.map.get(self.total, self.total)
        return [idx // self.n, idx % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.map.clear()
