# 题目剑指 Offer 42：
# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
#
# 要求时间复杂度为O(n)。
#
# 示例1:
#
# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释:连续子数组[4,-1,2,1] 的和最大，为6。

# 题解1：（动态规划）
# 思路：设f[i]为以nums[i]结尾的数组的最大值，则根据动态规划可得：f[i] = max(nums[i], f[i-1]+nums[i])
def maxSubArray(self, nums: list[int]) -> int:
    answer = nums[0]
    f = [answer for i in nums]
    for i in range(1, len(nums)):
        f[i] = max(nums[i], f[i - 1] + nums[i])
        answer = max(answer, f[i])
    return answer


# 题解2：（前缀和算法）
# 思路：该题的解题方法只需要求出前缀和，最大值为前缀和减去之前前缀和的最小值，但是之前前缀和最大值为0则为前缀和

def maxSubArray(self, nums: list[int]) -> int:
    answer = nums[0]
    sum_nums = 0
    min_nums = 0
    for i in nums:
        sum_nums += i
        answer = max(answer, sum_nums - min_nums)
        if sum_nums < min:
            min_nums = sum_nums
    return answer



