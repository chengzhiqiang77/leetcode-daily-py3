# _*_ coding = utf-8 _*_
# created by czq on 2021/10/25


# 题目240：
# 编写一个高效的算法来搜索mxn矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
#
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。


# 题解1：
# 思路：我们可以从最后一行的第一个开始查找，然后根据情况往上或往右遍历


def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    if n == 0:
        return False
    i = m - 1
    j = 0
    while i >= 0 and j < n:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            j = j + 1
        else:
            i = i - 1
    return False
