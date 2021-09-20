# _*_ coding = utf-8 _*_
# created by czq on 2021/9/20


# 题目673：
#
# 给定一个未排序的整数数组，找到最长递增子序列的个数。


# 题解1：
# 思路：该题目是个很经典的动态规划题目，我们设dp[i]为以nums[i]结尾的最长递增子序列的长度，cnt[i]为以nums[i]结尾的最长递增子序列的个数，我们
# 可以列出动态规划状态转移方程：dp[i]=max(dp[j])+1,其中0≤j<i且num[j]<num[i]，其中dp[0] = 1,我们可以写出题解


def findNumberOfLIS(self, nums: list[int]) -> int:
    n, max_len, answer = len(nums), 0, 0
    dp = [0] * n
    cnt = [0] * n
    for index, value in enumerate(nums):
        dp[index] = cnt[index] = 1
        for i in range(index):
            if value > nums[i]:
                if dp[i] + 1 > dp[index]:
                    dp[index] = dp[i] + 1
                    cnt[index] = cnt[i]
                elif dp[i] + 1 == dp[index]:
                    cnt[index] += cnt[i]
        if dp[index] > max_len:
            max_len = dp[index]
            answer = cnt[index]
        elif dp[index] == max_len:
            answer += cnt[index]
    return answer


