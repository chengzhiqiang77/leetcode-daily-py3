# _*_ coding = utf-8 _*_
# created by czq on 2021/11/17


# 题目391：
#
#
# 给你一个数组 rectangles ，其中 rectangles[i] = [xi, yi, ai, bi] 表示一个坐标轴平行的矩形。这个矩形的左下顶点是 (xi, yi) ，右上顶点是 (ai, bi) 。
#
# 如果所有矩形一起精确覆盖了某个矩形区域，则返回 true ；否则，返回 false 。


# 题解1：
# 思路：对于一个精准覆盖的矩形来说，每个小矩形体积相加等于所有大矩形的面积，算出所有小矩形中所有的顶点，其中大矩形的顶点出现为单数，其他顶点至少出现两次的偶数；
import collections
from math import inf


def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
    sum_all = 0
    left_up, left_down, right_up, right_down = -inf, inf, -inf, inf
    ans = collections.defaultdict(int)
    for i in rectangles:
        sum_all += abs((i[2] - i[0]) * (i[3] - i[1]))
        left_down = min(left_down, i[0])
        left_up = max(left_up, i[2])
        right_up = max(right_up, i[3])
        right_down = min(right_down, i[1])
        ans[i[0], i[1]] += 1
        ans[i[0], i[3]] += 1
        ans[i[2], i[1]] += 1
        ans[i[2], i[3]] += 1
    a = (left_down, right_down)
    b = (left_down, right_up)
    c = (left_up, right_down)
    d = (left_up, right_up)
    if abs((left_up - left_down) * (right_up - right_down)) != sum_all:
        return False
    if not (ans[a] * ans[b] * ans[c] * ans[d]):
        return False
    for i in ans:
        if ans[i] != 2 and ans[i] != 4:
            if i != a and i != b and i != c and i != d:
                return False

    return True
