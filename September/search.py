# _*_ coding = utf-8 _*_
# created by czq on 2021/9/6


# 题目704：
# 给定一个n个元素有序的（升序）整型数组nums 和一个目标值target ，写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。


# 题解1：
# 思路：该题目就是基础的二分查找，注意（left+right)的范围，可以使用left + (right - left)//2


def search(self, nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        if nums[mid] < target:
            left = mid + 1
    return -1
