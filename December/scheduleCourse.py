# _*_ coding = utf-8 _*_
# created by czq on 2021/12/14


# 题目630：
# 这里有 n 门不同的在线课程，按从 1 到 n编号。给你一个数组 courses ，其中 courses[i] = [durationi, lastDayi]
# 表示第 i 门课将会 持续 上 durationi 天课，并且必须在不晚于 lastDayi 的时候完成。
#
# 你的学期从第 1 天开始。且不能同时修读两门及两门以上的课程。
#
# 返回你最多可以修读的课程数目。


# 题解1：
# 思路：将课程按照结束时间排序，利用贪心的策略，选择不超过最晚日期的课程，当超过后，与已经选择的课程中的最大值进行对比即可；
import heapq


def scheduleCourse(self, courses: list[list[int]]) -> int:
    courses.sort(key=lambda x: x[1])
    target = 0
    q = []
    for time, deadline in courses:
        if target + time <= deadline:
            target += time
            heapq.heappush(q, -time)
        elif q and -q[0] > time:
            target -= -q[0] - time
            heapq.heappop(q)
            heapq.heappush(q, -time)
    return len(q)
