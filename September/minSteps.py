# _*_ coding = utf-8 _*_
# created by czq on 2021/9/19


# 题目650：
# 最初记事本上只有一个字符 'A' 。你每次可以对这个记事本进行两种操作：
#
# Copy All（复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。
# Paste（粘贴）：粘贴 上一次 复制的字符。
# 给你一个数字n ，你需要使用最少的操作次数，在记事本上输出 恰好n个 'A' 。返回能够打印出n个 'A' 的最少操作次数。


# 题解1：
# 思路：对于复制粘贴操作，就是将原来的字符变为原来的x+1倍，对n进行拆分


def minSteps(self, n: int) -> int:
    res = 0
    for i in range(2, n + 1):
        while n % i == 0:
            res += i
            n /= i
    return res
