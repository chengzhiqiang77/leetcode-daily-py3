# _*_ coding = utf-8 _*_
# created by czq on 2021/11/12


# 题目629：
# 给出两个整数n和k，找出所有包含从1到n的数字，且恰好拥有k个逆序对的不同的数组的个数。
#
# 逆序对的定义如下：对于数组的第i个和第j个元素，如果满i<j且a[i]>a[j]，则其为一个逆序对；否则不是。
#
# 由于答案可能很大，只需要返回 答案 mod 109+ 7 的值。


# 题解1：
# 思路：5555，不会动态规划！！！！写不出状态转移方程


def kInversePairs(self, n: int, k: int) -> int:
    mod = 10 ** 9 + 7
    f = [1] + [0] * k
    for i in range(1, n + 1):
        g = [0] * (k + 1)
        for j in range(k + 1):
            g[j] = (g[j - 1] if j - 1 >= 0 else 0) - (f[j - i] if j - i >= 0 else 0) + f[j]
            g[j] %= mod
        f = g

    return f[k]
