# _*_ coding = utf-8 _*_
# created by czq on 2021/10/1


# 题目223：
#
# 给你 二维 平面上两个 由直线构成的 矩形，请你计算并返回两个矩形覆盖的总面积。
#
# 每个矩形由其 左下 顶点和 右上 顶点坐标表示：
#
# 第一个矩形由其左下顶点 (ax1, ay1) 和右上顶点 (ax2, ay2) 定义。
# 第二个矩形由其左下顶点 (bx1, by1) 和右上顶点 (bx2, by2) 定义


# 题解1：
# 思路：要算重叠的矩形的面积，我们可以将两个矩形的面积求出来，然后求出实际在平面上的面积，两个相减就是重叠的面积


def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)
    overlapWidth = min(ax2, bx2) - max(ax1, bx1)
    overlapHeight = min(ay2, by2) - max(ay1, by1)
    overlapArea = max(overlapWidth, 0) * max(overlapHeight, 0)
    return area1 + area2 - overlapArea
