# _*_ coding = utf-8 _*_
# created by czq on 2022/1/2


# 题目1995：
# 给你一个 下标从 0 开始 的整数数组 nums ，返回满足下述条件的 不同 四元组 (a, b, c, d) 的 数目 ：
#
# nums[a] + nums[b] + nums[c] == nums[d] ，且
# a < b < c < d


# 题解1：
# 思路：遍历这个列表，然后取不同的数字相加看是否符合四元祖的的定义；


def countQuadruplets(self, nums: list[int]) -> int:
    n = len(nums)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for z in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] == nums[z]:
                        ans += 1
    return ans
