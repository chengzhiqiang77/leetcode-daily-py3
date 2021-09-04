# _*_ coding = utf-8 _*_
# created by czq on 2021/9/4


# 题目剑指offer 10- I：
# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
#
# F(0) = 0, F(1)= 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
#
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。


# 题解1：
# 思路：由公式可得到答案


def fib(self, n: int) -> int:
    mod = 1000000007
    first, second = 0, 0
    answer = 1
    if n < 2:
        return n
    for i in range(2, n + 1):
        first = second
        second = answer
        answer = (first + answer) % mod
    return answer
