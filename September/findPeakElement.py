# _*_ coding = utf-8 _*_
# created by czq on 2021/9/15


# 题目162：
# 峰值元素是指其值严格大于左右相邻值的元素。
#
# 给你一个整数数组nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
#
# 你可以假设nums[-1] = nums[n] = -∞ 。
#
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。


# 题解1：
# 思路：题目中要求时间复杂度为O(logn)，我们能想到二分，但是这题目怎么使用二分呢，因为二分是个要求列表为有序的算法，但是题目所给的列表是无序的，
# 但是我们可以注意到，题目假设nums[-1],nums[n] = -inf，所以我们可以得到，随机选取一个数，当num[i] < nums[i+1]，则i右侧一定存在峰值，反之
# 则在左侧一定存在峰值


def findPeakElement(self, nums: list[int]) -> int:
    nums.append(nums[-1] - 1)
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (right + left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        elif nums[mid] >= nums[mid + 1]:
            right = mid
    return left
