# _*_ coding = utf-8 _*_
# created by czq on 2021/8/11


# 题目446：
# 给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。
#
# 如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。
#
# 例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。
# 再例如，[1, 1, 2, 5, 7] 不是等差序列。
# 数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。
#
# 例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
# 题目数据保证答案是一个 32-bit 整数


# 题解1：
# 思路：我们可以依次从第一个元素开始，开始找存在第j个元素，是否存在j-n这个差值，在其他的元素的diff中
# 存在，如果存在，则满足等差数列，根据昨天题目的推导可得状态转移方程ans += cnt + 1
import collections


def numberOfArithmeticSlices(self, nums: list[int]) -> int:
    # 由昨天的题目推导可得状态转移方程：ans += cnt + 1
    n = len(nums)
    answer = 0
    dp = [collections.Counter() for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            diff = nums[j] - nums[i]
            cnt = dp[i][diff]
            answer += cnt
            dp[j][diff] += cnt + 1
    return answer
