# _*_ coding = utf-8 _*_
# created by czq on 2021/8/23


# 题目1646：
# 给你一个整数 n 。按下述规则生成一个长度为 n + 1 的数组 nums ：
#
# nums[0] = 0
# nums[1] = 1
# 当 2 <= 2 * i <= n 时，nums[2 * i] = nums[i]
# 当 2 <= 2 * i + 1 <= n 时，nums[2 * i + 1] = nums[i] + nums[i + 1]
# 返回生成数组 nums 中的 最大 值。


# 题解1：
# 思路：直接模拟数组，然后返回数组中最大值即可


def getMaximumGenerated(self, n: int) -> int:
    nums = [0 for _ in range(n + 1)]
    for i in range(n + 1):
        if i == 0:
            nums[i] = 0
        elif i == 1:
            nums[i] = 1
        elif i % 2 == 0:
            nums[i] = nums[i // 2]
        else:
            nums[i] = nums[i // 2] + nums[i // 2 + 1]
    return max(nums)
