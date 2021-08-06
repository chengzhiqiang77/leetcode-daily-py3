# _*_ coding = utf-8 _*_
# created by czq on 2021/8/6


# 题目74：
# 编写一个高效的算法来判断m x n矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。


# 题解1：
# 思路：将这个矩阵转换为一个列表，判断target是否在列表中即可


def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    answer = []
    for i in matrix:
        answer.extend(i)
    return target in answer


# 题解2：
# 思路：将矩阵转换为列表后，可以得到一个有序的列表，这个适合，我们可以使用二分查找来寻找元素是否存在在列表中


def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    def binary_search(li, val):
        left = 0
        right = len(li) - 1
        while left <= right:
            mid = (left + right) // 2
            if li[mid] == val:
                return mid
            elif li[mid] > val:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return -1
    answer = []
    for i in matrix:
        answer.extend(i)
    n = binary_search(answer, target)
    return False if n == -1 else True
