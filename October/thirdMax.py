# _*_ coding = utf-8 _*_
# created by czq on 2021/10/7


# 题目414：
# 给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。


# 题解1：
# 思路：维护三个值，分别为最大值，第二大的值，和第三大的值，只需要遍历一次数组，即可得出答案
from math import inf


def thirdMax(self, nums: list[int]) -> int:
    first = -inf
    second = -inf
    thrid = -inf
    for num in nums:
        if num > first:
            first, second, thrid = num, first, second
        elif first > num > second:
            second, thrid = num, second
        elif second > num > thrid:
            thrid = num
    return thrid if thrid != -inf else first
