# _*_ coding = utf-8 _*_
# created by czq on 2021/8/13


# 题目233：
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。


# 题解1：
# 思路：公式来源于官方题解。。。。

def countDigitOne(self, n: int) -> int:
    sqrt = 1
    answer = 0
    while n >= sqrt:
        answer += (n // (sqrt * 10)) * sqrt + min(max(n % (sqrt * 10) - sqrt + 1, 0), sqrt)
        sqrt *= 10
    return answer
