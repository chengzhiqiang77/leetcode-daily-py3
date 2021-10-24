# _*_ coding = utf-8 _*_
# created by czq on 2021/10/24


# 题目66：
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。


# 题解1：
# 思路：从后往前遍历数组，找出最后为9的后缀进行特殊处理即可


def plusOne(self, digits: list[int]) -> list[int]:
    list_length = len(digits)
    for i in range(list_length - 1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            for j in range(i + 1, list_length):
                digits[j] = 0
            return digits
    return [1] + [0] * list_length
