# _*_ coding = utf-8 _*_
# created by czq on 2021/10/20


# 题目453：
# 给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。


# 题解1：
# 思路：设操作数为k，设最后元素为target，我们可以得到一个等式，target * n = k(n-1) + sum(nums),且target为min(nums)+k,
# 则可以得到（min(nums) + k) * n = k (n - 1) + sum(nums),化简可以得到k = sum(nums) - n*min(sums)


def minMoves(self, nums: list[int]) -> int:
    return sum(nums) - len(nums) * min(nums)
