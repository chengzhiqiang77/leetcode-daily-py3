# _*_ coding = utf-8 _*_
# created by czq on 2021/9/11


# 题目600：
# 给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。


# 题解1：
# 思路：对于前缀包含了11的，则不管后缀怎么组合，都不满足条件，如果前缀不包含11的，则后缀可能的答案呈斐波那契数列


def findIntegers(self, n: int) -> int:
    n += 1
    a, b, s = 1, 1, 0
    while n > 0:
        if n % 4 == 3:
            s = b
        elif n % 4 == 1:
            s += b
        n //= 2
        b, a = a + b, b
    return s
