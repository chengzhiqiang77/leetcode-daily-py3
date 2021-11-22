# _*_ coding = utf-8 _*_
# created by czq on 2021/11/22


# 题目594：
# 和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。
#
# 现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。
#
# 数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。


# 题解1：
# 思路：对数组内元素进行统计，枚举所有可能的情况，取其中长度最长的即可
import collections


def findLHS(self, nums: list[int]) -> int:
    ans = collections.Counter(nums)
    res = 0
    for i in ans:
        res_i = 0
        if ans[i - 1] != 0:
            res_i = max(res_i, ans[i - 1] + ans[i])
        if ans[i + 1] != 0:
            res_i = max(res_i, ans[i] + ans[i + 1])
        res = max(res, res_i)
    return res
