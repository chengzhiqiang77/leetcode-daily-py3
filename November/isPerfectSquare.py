# _*_ coding = utf-8 _*_
# created by czq on 2021/11/4


# 题目367：
# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
#
# 进阶：不要 使用任何内置的库函数，如 sqrt 。


# 题解1：
# 思路：利用二分法找平方数即可


def isPerfectSquare(self, num: int) -> bool:
    left, right = 1, num
    while left <= right:
        mid = (left + right) // 2
        temp = mid * mid
        if temp == num:
            return True
        if temp < num:
            left = mid + 1
        else:
            right = mid - 1
    return False
