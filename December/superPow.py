# _*_ coding = utf-8 _*_
# created by czq on 2021/12/10


# 题目372：
# 你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。


# 题解1：
# 思路：利用快速幂的思想，求出答案然后对1337取模即可；


def superPow(self, a: int, b: list[int]) -> int:
    MOD = 1337
    ans = 1
    for e in reversed(b):
        ans = ans * pow(a, e, MOD) % MOD
        a = pow(a, 10, MOD)
    return ans
