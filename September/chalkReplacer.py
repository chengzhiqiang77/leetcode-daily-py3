# _*_ coding = utf-8 _*_
# created by czq on 2021/9/10


# 题目1894：
# 一个班级里有n个学生，编号为 0到 n - 1。每个学生会依次回答问题，编号为 0的学生先回答，然后是编号为 1的学生，以此类推，
# 直到编号为 n - 1的学生，然后老师会重复这个过程，重新从编号为 0的学生开始回答问题。
#
# 给你一个长度为 n且下标从 0开始的整数数组chalk和一个整数k。一开始粉笔盒里总共有k支粉笔。当编号为i的学生回答问题时，
# 他会消耗 chalk[i]支粉笔。如果剩余粉笔数量 严格小于chalk[i]，那么学生 i需要 补充粉笔。
#
# 请你返回需要 补充粉笔的学生 编号。


# 题解1：
# 思路：学生消耗粉笔的数量一轮下来是固定的，我们只需要粉笔总数对学生一轮消耗的总数进行取模，剩下的粉笔数再进行一轮，必定能找到一个学生的粉笔数不足
import bisect


def chalkReplacer(self, chalk: list[int], k: int) -> int:
    sum_chalk = sum(chalk)
    target = k % sum_chalk
    for index, value in enumerate(chalk):
        target -= value
        if target < 0:
            return index


# 题解2：
# 思路：思路和题解1的类似，只是对于查找的时候，先算出前缀和列表，然后在列表中使用二分查找


def chalkReplacer(self, chalk: list[int], k: int) -> int:
    for i in range(len(chalk)):
        if i != 0:
            chalk[i] += chalk[i-1]
    target = k % chalk[-1]
    return bisect.bisect_right(chalk, target)