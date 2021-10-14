# _*_ coding = utf-8 _*_
# created by czq on 2021/10/14


# 题目 剑指offer2 II 069：
# 符合下列属性的数组 arr 称为 山峰数组（山脉数组） ：
#
# arr.length >= 3
# 存在 i（0 < i< arr.length - 1）使得：
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# 给定由整数组成的山峰数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 的下标 i，即山峰顶部。


# 题解1：
# 思路：由于山峰数组中的山峰顶部只有一个，所有我们可以使用二分不断逼近山峰


def peakIndexInMountainArray(self, arr: list[int]) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return mid
        elif arr[mid] < arr[mid + 1]:
            left = mid + 1
        elif arr[mid] < arr[mid - 1]:
            right = mid - 1
