# _*_ coding = utf-8 _*_
# created by czq on 2021/9/13


# 题目447：
# 给定平面上n 对 互不相同 的点points ，其中 points[i] = [xi, yi] 。回旋镖 是由点(i, j, k) 表示的元组 ，
# 中i和j之间的距离和i和k之间的距离相等（需要考虑元组的顺序）。
#
# 返回平面上所有回旋镖的数量。


# 题解1：
# 思路：题目中所说的i和j的距离与i和k的距离是相等的，我们可以把i看作目标点，其余两个点与他的距离是相等的，这样三点，就可以构成一个回旋镖，
# 而我们需要注意到，由于元祖的顺序会影响到回旋镖，所以，j和k互换位置的话，也构成了一个新的回旋镖，我们可以得到，如果此时有n个点与i的距离是相等的，
# 那么可以构成，我们可以用数学归纳法得出，回旋镖的数量 = n * (n - 1)；至此，我们可以用哈希表存储目标点与其余点的距离的个数，算出回旋镖的数量
import collections


def numberOfBoomerangs(self, points: list[list[int]]) -> int:
    ans = 0
    for point_start in points:
        answer = collections.defaultdict(int)
        for point_end in points:
            load = (point_start[0] - point_end[0]) * (point_start[0] - point_end[0]) + (
                        point_start[1] - point_end[1]) * (point_start[1] - point_end[1])
            answer[load] += 1
        for val in answer.values():
            ans += val * (val - 1)
    return ans