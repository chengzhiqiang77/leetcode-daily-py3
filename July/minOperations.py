# _*_ coding = utf-8 _*_
# created by czq on 2021/7/26


# 题目1713：
# 给你一个数组target，包含若干 互不相同的整数，以及另一个整数数组arr，arr可能 包含重复元素。
#
# 每一次操作中，你可以在 arr的任意位置插入任一整数。比方说，如果arr = [1,4,1,2]，那么你可以在中间添加 3得到[1,4,3,1,2]
# 。你可以在数组最开始或最后面添加整数。
#
# 请你返回 最少操作次数，使得target成为arr的一个子序列。
#
# 一个数组的 子序列指的是删除原数组的某些元素（可能一个元素都不删除），同时不改变其余元素的相对顺序得到的数组。比方说，[2,7,4]是
# [4,2,3,7,2,1,4]的子序列（加粗元素），但[2,4,2]不是子序列。


# 题解1：
# 思路：可以把arr中的元素转为在target中的下标，这样，问题可以简化为求其中最长严格递增公共子序列的长度
import bisect


def minOperations(self, target: list[int], arr: list[int]) -> int:
    dic = dict()
    for i, x in enumerate(target):
        dic[x] = i

    nums = []
    for x in arr:
        if x in dic:
            nums.append(dic[x])

    if not nums:
        return len(target)

    a = []
    for x in nums:
        i = bisect.bisect_left(a, x)
        if i == len(a):
            a.append(x)
        else:
            a[i] = x

    return len(target) - len(a)
