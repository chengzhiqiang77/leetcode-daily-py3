# 题目1893：
# 给你一个二维整数数组ranges和两个整数left和right。每个ranges[i] = [starti, endi]表示一个从starti到endi的闭区间。
#
# 如果闭区间[left, right]内每个整数都被ranges中至少一个区间覆盖，那么请你返回true，否则返回false。
#
# 已知区间 ranges[i] = [starti, endi] ，如果整数 x 满足 starti <= x <= endi，那么我们称整数x被覆盖了


# 题解1：
# 思路：对于每个闭区间，只要left比starti大比endi小，则可以更新left，只要left大于right，则全部数字被闭区间覆盖了


def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
    ranges.sort()
    for i in ranges:
        if i[0] <= left <= i[1]:
            left = i[1] + 1
    return left > right
