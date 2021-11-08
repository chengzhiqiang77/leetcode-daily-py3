# _*_ coding = utf-8 _*_
# created by czq on 2021/11/8


# 题目268：
# 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。


# 题解1：
# 思路：算出0-n的总和，然后遍历这个数组，用总和减去元素，最后剩下的数字就是没有出在数组中的那个数字


def missingNumber(self, nums: list[int]) -> int:
    n = len(nums)
    target = n * (n + 1) // 2
    for i in nums:
        target -= i
    return target
