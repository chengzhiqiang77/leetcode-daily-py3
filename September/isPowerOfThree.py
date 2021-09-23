# _*_ coding = utf-8 _*_
# created by czq on 2021/9/23


# 题目326：
# 给定一个整数，写一个函数来判断它是否是 3的幂次方。如果是，返回 true ；否则，返回 false 。
#
# 整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x


# 题解1；
# 思路：对给定的数字除3，直到数字小于三，为了减少循环次数，我们在每次除3之后，可以判断该数模3是否为0


def isPowerOfThree(self, n: int) -> bool:
    if n == 0:
        return False
    while n != 1:
        a = n % 3
        n /= 3
        if a != 0:
            return False
    return True
