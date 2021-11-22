# _*_ coding = utf-8 _*_
# created by czq on 2021/11/22


# 题目384：
# 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。
#
# 实现 Solution class:
#
# Solution(int[] nums) 使用整数数组 nums 初始化对象
# int[] reset() 重设数组到它的初始状态并返回
# int[] shuffle() 返回数组随机打乱后的结果


# 题解1：
# 思路：该题目最重要的是在于设计shuffle算法，只需要每次在列表中随机抽出一个数字即可
import copy
import random


class Solution:

    def __init__(self, nums: list[int]):
        self.arr = nums

    def reset(self) -> list[int]:
        return self.arr

    def shuffle(self) -> list[int]:
        res = copy.deepcopy(self.arr)
        n = len(res)
        for i in range(n):
            idx = random.randint(i, n - 1)
            res[i], res[idx] = res[idx], res[i]
        return res
