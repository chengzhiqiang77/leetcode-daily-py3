# _*_ coding = utf-8 _*_
# created by czq on 2021/8/8


# 题目1137：
# 泰波那契序列Tn定义如下：
#
# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0的条件下 Tn+3 = Tn + Tn+1 + Tn+2
#
# 给你整数n，请返回第 n 个泰波那契数Tn 的值。


# 题解1：
# 思路：该题目已经给出了动态规划递推公示，直接使用即可


def tribonacci(self, n: int) -> int:
    answer = [1 for _ in range(n+1)]
    for i in range(n+1):
        if i == 0:
            answer[0] = 0
        elif i == 1 or i == 2:
            answer[i] = 1
        else:
            answer[i] = answer[i-3] + answer[i-2] + answer[i-1]
    return answer[n]


def tribonacci(self, n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    t0, t1, t2 = 0, 1, 1
    for i in range(3, n + 1):
        tmp = t0 + t1 + t2
        t0, t1, t2 = t1, t2, tmp
    return t2
