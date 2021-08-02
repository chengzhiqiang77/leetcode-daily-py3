# _*_ coding = utf-8 _*_
# created by czq on 2021/8/1


# 题目1337：
# 给你一个大小为m* n的矩阵mat，矩阵由若干军人和平民组成，分别用 1 和 0 表示。
#
# 请你返回矩阵中战斗力最弱的k行的索引，按从最弱到最强排序。
#
# 如果第i行的军人数量少于第j行，或者两行军人数量相同但 i 小于 j，那么我们认为第 i 行的战斗力比第 j 行弱。
#
# 军人 总是 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。


# 题解1：
# 思路：mat列表中，军人总是在靠前的位置，所以队列为顺序队列，可以通过二分法求出每个队列的军人数量，由题目可得，矩阵
# 的长度不超过100，可以吧军人数量*100加上该队列所在的索引位置
import bisect


def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
    answer = []
    answerIndex = []
    answerNum = []
    x = 0
    for i in range(len(mat)):
        mat[i].reverse()
        x = bisect.bisect_left(mat[i], 1)
        answer.append(x * 100 - i)
    for i, j in enumerate(answer):
        answerIndex.append([j, i])
    answerIndex.sort(reverse=True)
    for i in range(k):
        answerNum.append(answerIndex[i][1])
    return answerNum

