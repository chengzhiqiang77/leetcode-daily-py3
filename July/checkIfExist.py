# 题目1346：
# 给你一个整数数组arr，请你检查是否存在两个整数N 和 M，满足N是M的两倍（即，N = 2 * M）。
#
# 更正式地，检查是否存在两个下标i 和 j 满足：
#
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]


# 题解1：
# 思路：遍历两次这个数组，判断是否存在M = 2 * N，需要满足的条件为，M/N一个数不为0
import collections


def checkIfExist(self, arr: list[int]) -> bool:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] * 2 == arr[j] and i != j:
                if arr[i] != arr[j] and (arr[i] == 0 or arr[j] == 0):
                    continue
                else:
                    return True
    return False


# 题解2：
# 思路：利用哈希表记录数组中每个数字的出现次数，遍历这个数组，如果哈希表中对应数字的出现次数大于1，则存在MN满足条件，
# 对于0要特殊处理


def checkIfExist(self, arr: list[int]) -> bool:
    nums = collections.Counter(arr)
    for i in arr:
        if i != 0 and nums[2 * i] >= 1:
            return True
        if i == 0 and nums[0] >= 2:
            return True
    return False
