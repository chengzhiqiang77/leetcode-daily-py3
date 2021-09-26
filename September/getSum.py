# _*_ coding = utf-8 _*_
# created by czq on 2021/9/26


# 题目371：
# 给你两个整数 a 和 b ，不使用 运算符 + 和 -，计算并返回两整数之和。


# 题解1：
# 思路：这题的本质就是让我们实现计算机的加法器，我们可以得知，计算器中的加法就是异或运算加上需要加的进位，进位可以用与运算然后移位来实现，
# 但是对于python来说，由于没有限制长度，所以我们需要特殊进行处理


def getSum(self, a: int, b: int) -> int:
    MASK = 4294967296
    # 整型最大值
    MAX_INT = 2147483647
    MIN_INT = 2147483648
    while b != 0:
        tmp = (a & b) << 1 % MASK
        a = (a ^ b) % MASK
        b = tmp
    if a >= MAX_INT:
        return ~((a ^ MAX_INT) ^ MIN_INT)
    else:
        return a
