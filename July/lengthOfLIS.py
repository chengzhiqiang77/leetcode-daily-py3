# _*_ coding = utf-8 _*_
# created by czq on 2021/7/26


# 题目300：
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。


# 题解1：
# 思路：如果我们要使上升子序列尽可能的长，则我们需要让序列上升得尽可能慢，因此我们希望每次在上升子序列最后加上的那个数尽可能的小，
# 基于上面的思想，维护一个有序数组，用len记录目前最长上升子序列的长度
import bisect


def lengthOfLIS(self, nums: list[int]) -> int:
    a = []
    for x in nums:
        i = bisect.bisect_left(a, x)
        if i == len(a):
            a.append(x)
        else:
            a[i] = x
    return len(a)
