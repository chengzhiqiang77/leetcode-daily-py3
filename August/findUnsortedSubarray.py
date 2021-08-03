# _*_ coding = utf-8 _*_
# created by czq on 2021/8/3


# 题目581：
# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
# 请你找出符合题意的 最短 子数组，并输出它的长度。


# 题解1：
# 思路：将nums进行排序，维护left和right为最短子数组的左右节点，排序后的nums与排序前的nums对比即可求出左右节点


def findUnsortedSubarray(self, nums: list[int]) -> int:
    nums_copy = sorted(nums)
    left = 0
    right = len(nums) - 1
    while left < len(nums) and nums_copy[left] == nums[left]:
        left += 1
    while right >= 0 and nums_copy[right] == nums[right]:
        right -= 1
    if left == len(nums):
        return 0
    else:
        return right - left + 1
