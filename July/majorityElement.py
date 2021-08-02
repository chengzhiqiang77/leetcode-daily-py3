# 题目 面试题17.10：
# 数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。
#
# 示例 1：
#
# 输入：[1,2,5,9,5,9,5,5,5]
# 输出：5
# 示例 2：
#
# 输入：[3,2]
# 输出：-1
# 示例 3：
#
# 输入：[2,2,1,1,1,2,2]
# 输出：2


# 题解1：
# 思路：获取数组中各个元素出现的频率，如果存在元素的频率大于数组长度的一半，则返回该元素，如果不存在元素的频率大于数组长度的一半，则返回-1
import collections


def majorityElement(self, nums: list[int]) -> int:
    sum = len(nums)
    m = collections.Counter(nums)
    # m = sorted(m.items(), key=lambda items: items[1], reverse=True)
    # if len(m) == 0:
    #     return -1
    # if len(m) == 1:
    #     return m[0][0]
    for key, value in m.items():
        if value >= sum / 2:
            return key
    return -1
    # if sum/m[0][1] <= 2:
    #     return m[0][0]
    # if sum/m[0][1] > 2:
    #     return -1


# 题解2：
# 思路：投票法（待研究学习）
# 在每一轮投票中，删除两个不同的数字，最后剩下的元素可能为主要元素，由于可能存在没有主要元素的情况，对获得的元素进行计数，大于数组长度的
# 一半，则为主要元素


def majorityElement(self, nums: list[int]) -> int:
    condictions = 0
    count = 0
    sum = 0
    for i in nums:
        if count == 0:
            condictions = i
            count = 1
        elif condictions == i:
            count += 1
        elif condictions != i:
            count -= 1
    if count == 0:
        return -1
    for i in nums:
        if condictions == i:
            sum += 1
    if sum >= len(nums)/2:
        return condictions
    else:
        return -1

