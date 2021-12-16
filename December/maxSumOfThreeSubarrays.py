# _*_ coding = utf-8 _*_
# created by czq on 2021/12/16


# 题目689：
# 给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且全部数字和（3 * k 项）最大的子数组，并返回这三个子数组。
#
# 以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。


# 题解1：
# 思路：建立三个滑动窗口，三个滑动窗口分别从0，k，2k开始，依次往右滑动，维护第一个窗口最大值，第一个+第二个最大值，第二个+第一个+第三个最大值，
# 相应的，记录下他们的位置；


def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
    ans = []
    sum1, maxSum1, maxSum1Idx = 0, 0, 0
    sum2, maxSum12, maxSum12Idx = 0, 0, ()
    sum3, maxTotal = 0, 0
    for i in range(k * 2, len(nums)):
        sum1 += nums[i - k * 2]
        sum2 += nums[i - k]
        sum3 += nums[i]
        if i >= k * 3 - 1:
            if sum1 > maxSum1:
                maxSum1 = sum1
                maxSum1Idx = i - k * 3 + 1
            if maxSum1 + sum2 > maxSum12:
                maxSum12 = maxSum1 + sum2
                maxSum12Idx = (maxSum1Idx, i - k * 2 + 1)
            if maxSum12 + sum3 > maxTotal:
                maxTotal = maxSum12 + sum3
                ans = [*maxSum12Idx, i - k + 1]
            sum1 -= nums[i - k * 3 + 1]
            sum2 -= nums[i - k * 2 + 1]
            sum3 -= nums[i - k + 1]
    return ans
