# _*_ coding = utf-8 _*_
# created by czq on 2021/11/1


# 题目260：
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。


# 题解1：
# 思路：利用哈希表统计每个元素出现的次数，返回次数为1的元素即可；
import collections


def singleNumber(self, nums: list[int]) -> list[int]:
    ans = collections.Counter(nums)
    res = []
    for key, value in ans.items():
        if value == 1:
            res.append(key)
    return res
