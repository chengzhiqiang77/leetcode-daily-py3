# _*_ coding = utf-8 _*_
# created by czq on 2021/12/16


# 题目911：
# 给你两个整数数组 persons 和 times 。在选举中，第i张票是在时刻为times[i]时投给候选人 persons[i]的。
#
# 对于发生在时刻 t 的每个查询，需要找出在t 时刻在选举中领先的候选人的编号。
#
# 在t 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。
#
# 实现 TopVotedCandidate 类：
#
# TopVotedCandidate(int[] persons, int[] times) 使用persons 和 times 数组初始化对象。
# int q(int t) 根据前面描述的规则，返回在时刻 t 在选举中领先的候选人的编号。


# 题解1：
# 思路：对persons进行预处理，返回为一个在time[i]时刻领先的候选人的列表，然后在q中使用二分查找，找到不大于传入的时刻的time[i]，返回相对应
# 的答案即可；
import bisect
import collections


class TopVotedCandidate:

    def __init__(self, persons: list[int], times: list[int]):
        n = len(times)
        cnts, cur = collections.defaultdict(int), None
        self.ans, self.times = [-1] * n, times
        for i in range(n):
            cnts[persons[i]] += 1
            if cur is None or cnts[persons[i]] >= cnts[cur]:
                cur = persons[i]
            self.ans[i] = cur

    def q(self, t: int) -> int:
        print(self.ans)
        return self.ans[bisect.bisect_right(self.times, t) - 1]
