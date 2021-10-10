# _*_ coding = utf-8 _*_
# created by czq on 2021/10/10


# 题目441：
# 你总共有n枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。
#
# 给你一个数字n ，计算并返回可形成 完整阶梯行 的总行数。


# 题解1：
# 思路：每一次迭代减去下一行要减去的值，记录减去的最大值


def arrangeCoins(self, n: int) -> int:
    i = 1
    n_sum = 1
    while n_sum <= n:
        ans = i
        i += 1
        n_sum += i
    return ans
