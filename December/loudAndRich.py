# _*_ coding = utf-8 _*_
# created by czq on 2021/12/21


# 题目851：
# 有一组 n 个人作为实验对象，从 0 到 n - 1 编号，其中每个人都有不同数目的钱，以及不同程度的安静值（quietness）。为了方便起见，我们将编号为x的人简称为 "personx"。
#
# 给你一个数组 richer ，其中 richer[i] = [ai, bi] 表示 personai比 personbi更有钱。另给你一个整数数组 quiet ，其中quiet[i] 是 person i 的安静值。richer 中所给出的数据 逻辑自洽（也就是说，在 person x 比 person y 更有钱的同时，不会出现 person y 比 person x 更有钱的情况 ）。
#
# 现在，返回一个整数数组 answer 作为答案，其中answer[x] = y的前提是，在所有拥有的钱肯定不少于personx的人中，persony是最安静的人（也就是安静值quiet[y]最小的人）。


# 题解1：
# 思路：利用深度优先搜索的思想，对数组进行预处理，输出一个在前提下成立的答案列表


def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
    n = len(quiet)
    g = [[] for _ in range(n)]
    for r in richer:
        g[r[1]].append(r[0])

    ans = [-1] * n

    def dfs(x: int):
        if ans[x] != -1:
            return
        ans[x] = x
        for y in g[x]:
            dfs(y)
            if quiet[ans[y]] < quiet[ans[x]]:
                ans[x] = ans[y]

    for i in range(n):
        dfs(i)
    return ans
