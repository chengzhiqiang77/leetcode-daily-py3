# _*_ coding = utf-8 _*_
# created by czq on 2021/11/8


# 题目1218：
# 给你一个整数数组arr和一个整数difference，请你找出并返回 arr中最长等差子序列的长度，该子序列中相邻元素之间的差等于 difference 。
#
# 子序列 是指在不改变其余元素顺序的情况下，通过删除一些元素或不删除任何元素而从 arr 派生出来的序列。


# 题解1：
# 思路：可以设dp[i]为以i做结尾的等差子序列的长度,dp[i] = dp[i-difference] + 1，dp[i-difference]默认为0；
import collections


def longestSubsequence(self, arr: list[int], difference: int) -> int:
    dp = collections.Counter()
    for i in arr:
        dp[i] = dp[i - difference] + 1
    return max(dp.values())
