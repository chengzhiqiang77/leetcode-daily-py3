# _*_ coding = utf-8 _*_
# created by czq on 2021/8/30


# 题目528：
# 给定一个正整数数组w ，其中w[i]代表下标 i的权重（下标从 0 开始），请写一个函数pickIndex，它可以随机地获取下标 i，选取下标 i的概率与w[i]成正比。
#
# 例如，对于 w = [1, 3]，挑选下标 0 的概率为 1 / (1 + 3)= 0.25 （即，25%），而选取下标 1 的概率为 3 / (1 + 3)= 0.75（即，75%）。
#
# 也就是说，选取下标 i 的概率为 w[i] / sum(w) 。


# 题解1：
# 思路：根据w的值，算出前缀和的列表li，随机选取一个在1～li[-1]的数，使用二分法找出改数字在列表li中的位置，输出索引即可
import bisect
import itertools
import random


class Solution:

    def __init__(self, w: list[int]):
        self.li = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        rand = random.randint(1, self.li[-1])
        return bisect.bisect_left(self.li, rand)
