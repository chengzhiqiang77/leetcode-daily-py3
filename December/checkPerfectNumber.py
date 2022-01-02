# _*_ coding = utf-8 _*_
# created by czq on 2022/1/2


# 题目507：
# 对于一个正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。
#
# 给定一个整数n，如果是完美数，返回 true，否则返回 false


# 题解1：
# 思路：枚举数字的正因子，然后判断相加是否相等即可，只需要枚举跟号n的数字，因为再往上的正因子，已经被包含在内了；


def checkPerfectNumber(self, num: int) -> bool:
    if num == 1:
        return False
    sum1 = 1
    d = 2
    while d * d <= num:
        if num % d == 0:
            sum1 += d
            if d * d < num:
                sum1 += num / d
        d += 1
    return sum1 == num
