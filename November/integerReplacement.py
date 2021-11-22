# _*_ coding = utf-8 _*_
# created by czq on 2021/11/22


# 题目397：
# 给定一个正整数n ，你可以做如下操作：
#
# 如果n是偶数，则用n / 2替换n 。
# 如果n是奇数，则可以用n + 1或n - 1替换n 。
# n变为 1 所需的最小替换次数是多少？


# 题解1：
# 对于任意数字来说，n/2比n-1对答案的贡献都大，所以当可以n/2的时候，所以优先n/2，当不能n/2的时候，如果n+1/2 / 2是可以进行的，就取n+1，反之则取n-1


def integerReplacement(self, n: int) -> int:
    a = 0
    while n > 1:
        if n / 2 == n // 2:
            a += 1
            n = n // 2
        elif n != 3 and (n + 1) & n == 0:
            n = n + 1
            a += 1
        elif n != 3 and (n + 1) % 4 == 0:
            n = n + 1
            n = n // 2
            a += 2
        else:
            n = n - 1
            a += 1
    return a
