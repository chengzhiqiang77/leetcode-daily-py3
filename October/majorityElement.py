# _*_ coding = utf-8 _*_
# created by czq on 2021/10/24


# 题目229：给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。


# 题解1：
# 思路：将这个数组中的每个元素出现次数统计出来，然后找出超过n/3的返回即可
import collections


def majorityElement(self, nums: list[int]) -> list[int]:
    ans = collections.Counter(nums)
    ans_n = len(nums) // 3
    res = []
    for key, value in ans.items():
        if value > ans_n:
            res.append(key)
    return res
