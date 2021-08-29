# _*_ coding = utf-8 _*_
# created by czq on 2021/8/29


# 题目1588：
# 给你一个正整数数组arr，请你计算所有可能的奇数长度子数组的和。
#
# 子数组 定义为原数组中的一个连续子序列。
#
# 请你返回 arr中 所有奇数长度子数组的和 。


# 题解1：
# 思路：求出所有奇数长度子数组，返回和


def sumOddLengthSubarrays(self, arr: list[int]) -> int:
    answer = 0
    for i in range(1, len(arr) + 1, 2):
        for j in range(len(arr) - i + 1):
            answer += sum(arr[j:j + i])
    return answer
