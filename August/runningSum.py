# _*_ coding = utf-8 _*_
# created by czq on 2021/8/28


# 题目1480：
#
# 给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
#
# 请返回 nums 的动态和。


# 题解1：
# 思路：新的数组中长度与原数组相同，值为前面元素的和


def runningSum(self, nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
