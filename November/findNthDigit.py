# _*_ coding = utf-8 _*_
# created by czq on 2021/11/30


# 题目400：
# 给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位上的数字。


# 题解1：
# 思路：位数为x的数字在序列中个数为pow(10, x-1) * 9，可以用这个规律找出对应的数字即可


def findNthDigit(self, n: int) -> int:
    i = 1
    cnt = 9
    while n > cnt * i:
        n -= cnt * i
        i += 1
        cnt *= 10
    return int(str(pow(10, i - 1) + n // i - 1)[-1]) if not n % i else int(str(pow(10, i - 1) + n // i)[n % i - 1])
