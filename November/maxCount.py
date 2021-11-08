# _*_ coding = utf-8 _*_
# created by czq on 2021/11/8


# 题目598：
# 给定一个初始元素全部为0，大小为 m*n 的矩阵M以及在M上的一系列更新操作。
#
# 操作用二维数组表示，其中的每个操作用一个含有两个正整数a 和 b 的数组表示，含义是将所有符合0 <= i < a 以及 0 <= j < b 的元素M[i][j]的值都增加 1。
#
# 在执行给定的一系列操作后，你需要返回矩阵中含有最大整数的元素个数。


# 题解1：
# 思路：只需要找出操作的最小单位即可


def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
    if ops:
        min_cols, min_rows = ops[0][0], ops[0][1]
        for i in ops:
            if i[0] < min_cols:
                min_cols = i[0]
            if i[1] < min_rows:
                min_rows = i[1]
        return min_rows * min_cols
    else:
        return m * n
