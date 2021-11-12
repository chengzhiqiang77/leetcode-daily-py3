# _*_ coding = utf-8 _*_
# created by czq on 2021/11/12


# 题目375：
# 我们正在玩一个猜数游戏，游戏规则如下：
#
# 我从1到 n 之间选择一个数字。
# 你来猜我选了哪个数字。
# 如果你猜到正确的数字，就会 赢得游戏 。
# 如果你猜错了，那么我会告诉你，我选的数字比你的 更大或者更小 ，并且你需要继续猜数。
# 每当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。如果你花光了钱，就会 输掉游戏 。
# 给你一个特定的数字 n ，返回能够 确保你获胜 的最小现金数，不管我选择那个数字 。


# 题解1：
# 思路：枚举每个数字下猜每个数字所对应的钱，利用递归求出答案，递归终止条件为当两个数字相同，此时猜数字不需要花费
from functools import lru_cache
from math import inf


def getMoneyAmount(self, n: int) -> int:
    dp = [[inf] * (n + 1) for _ in range(n + 1)]

    @lru_cache(None)
    def dfs(left, right):
        if left >= right:
            return 0
        ans = inf
        for i in range(left, right + 1):
            cur = max(dfs(left, i - 1), dfs(i + 1, right)) + i
            ans = min(ans, cur)
        return ans

    return dfs(1, n)
