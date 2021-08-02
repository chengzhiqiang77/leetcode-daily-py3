# 题目剑指 Offer 53 - I：
# 统计一个数字在排序数组中出现的次数。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2
# 示例2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0


# 题解1：
# 思路：利用counter方法计算出数组中每个数字的出现次数，输出该数字对应的出现次数即可；
import bisect
import collections


def search(self, nums: list[int], target: int) -> int:
    return collections.Counter(nums)[target]


# 题解2：
# 思路：因为给定的数组是一个排序数组，只需要使用二分法找出左边第一个出现该数字的索引位置，然后找出第二个出现该数字的索引位置，两个值相减，
# 得到的就是对应数字出现的次数；


def search(self, nums: list[int], target: int) -> int:
    return bisect.bisect_right(nums, target) - bisect.bisect_left(nums, target)