# _*_ coding = utf-8 _*_
# created by czq on 2021/12/21


# 题目475：
# 冬季已经来临。你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
#
# 在加热器的加热半径范围内的每个房屋都可以获得供暖。
#
# 现在，给出位于一条水平线上的房屋houses 和供暖器heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。
#
# 说明：所有供暖器都遵循你的半径标准，加热的半径也一样。


# 题解1：
# 思路：遍历所有的房子，维护这个房子和他左边供暖器的距离，和右边供暖器的距离，取一个最小值，最后取一个这个最小值中的最大值
import bisect
from math import inf


def findRadius(self, houses: list[int], heaters: list[int]) -> int:
    heaters.sort()
    n = len(heaters)
    res = 0
    ans = 0
    for house in houses:
        i = bisect.bisect_right(heaters, house)
        left = house - heaters[i - 1] if i - 1 < n else inf
        right = heaters[i] - house if i < n else inf
        ans = min(abs(left), abs(right))
        res = max(res, ans)
    return res
