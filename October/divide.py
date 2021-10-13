# _*_ coding = utf-8 _*_
# created by czq on 2021/10/13


# 题目29：
# 给定两个整数，被除数dividend和除数divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#
# 返回被除数dividend除以除数divisor得到的商。
#
# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2


# 题解1：
# 思路：除法的本质就是看diviend中存在几个divisor，我们使用一个循环，每次加上divisor，但是这样的话循环的次数可能会很大，可以每次循环的时候累
# 加上这个值，保证循环次数指数减少


def divide(self, dividend: int, divisor: int) -> int:
    mark = False
    if dividend * divisor < 0:
        mark = True
    dividend = abs(dividend)
    divisor = abs(divisor)
    remain = dividend
    res = 0
    while remain >= divisor:
        div = divisor
        cur = 1
        while div + div < remain:
            cur += cur
            div += div
        remain -= div
        res += cur
    if mark:
        res = -res
    if res >= 2 ** 31 or res < -(2 ** 31):
        return 2 ** 31 - 1
    else:
        return res
