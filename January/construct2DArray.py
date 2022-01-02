# _*_ coding = utf-8 _*_
# created by czq on 2022/1/2


# 题目2022：
#
# 给你一个下标从 0 开始的一维整数数组 original 和两个整数 m 和  n 。你需要使用 original 中 所有 元素创建一个 m 行 n 列的二维数组。
#
# original 中下标从 0 到 n - 1 （都 包含 ）的元素构成二维数组的第一行，下标从 n 到 2 * n - 1 （都 包含 ）的元素构成二维数组的第二行，依此类推。
#
# 请你根据上述过程返回一个 m x n 的二维数组。如果无法构成这样的二维数组，请你返回一个空的二维数组。


# 题解1：
# 思路：首先判断数组的长度是否符合n*m，然后进行转化即可 ；


def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
    return [] if len(original) != (n * m) else [[original[n * j + i] for i in range(n)] for j in range(m)]
