# 题目930：
# 给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。
#
# 子数组 是数组的一段连续部分。
#
#
# 示例 1：
#
# 输入：nums = [1,0,1,0,1], goal = 2
# 输出：4
# 解释：
# 有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1]
# 示例 2：
#
# 输入：nums = [0,0,0,0,0], goal = 0
# 输出：15

# 题解1：
# 思路：遍历数组，获取当前的索引前所有数组的和，把和存入字典中，出现频率作为字典值，当前索引之前能组成非空子数组的数量等于字典中当前的和-目标值
import collections


def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        res, cur = 0, 0
        dp = collections.Counter()
        dp[0] = 1
        for i in nums:
            cur += i
            res += dp[cur-goal]
            dp[cur] += 1
        return res


# 题解2：（超时，是否能优化）
# 思路：根据滑动窗口来做，先计算出当前数组的和sum[],sum[i]表示为数组num第i个的和，定义一个左边界和右边界，左边界不变，移动右边界，直到滑动窗口
# 的值比goal大，左边界右移


def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
    k = 0
    sum = [0 for i in range(len(nums))]
    for i in range(len(nums)):
        if i == 0:
            sum[0] = nums[0]
        else:
            sum[i] = sum[i - 1] + nums[i]
        if sum[0] == goal:
            k = 1
    for right in range(1, len(nums)):
        if sum[right] == goal:
            k += 1
        if sum[right] >= goal:
            for left in range(right):
                if sum[right] - sum[left] == goal:
                    k += 1
                if sum[right] - sum[left] < goal:
                    break
    return k