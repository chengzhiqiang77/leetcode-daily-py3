# 题目645：
# 集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。
#
# 给定一个数组 nums 代表了集合 S 发生错误后的结果。
#
# 请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

# 题解1：
# 思路：首先计算出数组中每个数字出现的频率，出现频率不等于1（等于2）的为重复的整数，由题意可得，丢失的数字肯定小于s的长度，遍历字典，字典值等于0的就是缺失的数字
import collections


def findErrorNums(self, nums: list[int]) -> list[int]:
    err = []
    m = collections.Counter(nums)
    for word in m:
        if m[word] == 2:
            err.append(word)
    for i in range(len(nums)):
        if i + 1 != err[0] and m[i + 1] == 0:
            err.append(i + 1)
    return err
