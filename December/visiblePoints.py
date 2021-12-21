# _*_ coding = utf-8 _*_
# created by czq on 2021/12/21


# 题目1610：
# 给你一个点数组 points 和一个表示角度的整数 angle ，你的位置是 location ，其中 location = [posx, posy] 且 points[i] = [xi, yi] 都表示 X-Y 平面上的整数坐标。
#
# 最开始，你面向东方进行观测。你 不能 进行移动改变位置，但可以通过 自转 调整观测角度。换句话说，posx 和 posy 不能改变。你的视野范围的角度用 angle 表示， 这决定了你观测任意方向时可以多宽。设 d 为你逆时针自转旋转的度数，那么你的视野就是角度范围 [d - angle/2, d + angle/2] 所指示的那片区域。


# 题解1：
# 思路：对这个位置与点数组内进行对比，输出一个表示之间角度正切值，而后通过遍历找到这个点数组中，在角度的前提下，可以满足的最大数量是多少，还需要考虑
# 点和位置在同一个位置上的情况；
from bisect import bisect_right
from math import pi, atan2


def visiblePoints(self, points: list[list[int]], angle: int, location: list[int]) -> int:
    sameCnt = 0
    polarDegrees = []
    for p in points:
        if p == location:
            sameCnt += 1
        else:
            polarDegrees.append(atan2(p[1] - location[1], p[0] - location[0]))
    polarDegrees.sort()

    n = len(polarDegrees)
    polarDegrees += [deg + 2 * pi for deg in polarDegrees]
    print(polarDegrees)

    degree = angle * pi / 180
    print(degree)
    maxCnt = max((bisect_right(polarDegrees, polarDegrees[i] + degree) - i for i in range(n)), default=0)
    return maxCnt + sameCnt
