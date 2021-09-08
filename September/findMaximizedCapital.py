# _*_ coding = utf-8 _*_
# created by czq on 2021/9/8


# 题目502：
# 假设 力扣（LeetCode）即将开始 IPO 。为了以更高的价格将股票卖给风险投资公司，力扣 希望在 IPO 之前开展一些项目以增加其资本。 由于资源有限，
# 它只能在 IPO 之前完成最多 k 个不同的项目。帮助 力扣 设计完成最多 k 个不同项目后得到最大总资本的方式。
#
# 给你 n 个项目。对于每个项目 i ，它都有一个纯利润 profits[i] ，和启动该项目需要的最小资本 capital[i] 。
#
# 最初，你的资本为 w 。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。
#
# 总而言之，从给定项目中选择 最多 k 个不同项目的列表，以 最大化最终资本 ，并输出最终可获得的最多资本。
#
# 答案保证在 32 位有符号整数范围内。


# 题解1：
# 思路：对与资本w来说，进行一次投资后，只会增加不会减少，所以我们每次投资只需要选择满足当前资本可以获取利润最多的即可，这是经典的topk问题，
# 只是一个带条件的topk问题，我们只需要建大根堆，来求解问题即可，python中提供heapq库，但是建立的是小根堆，我们可以吧利润乘以-1，从而满足题意
import heapq


def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    answer = []
    cur = 0
    ans = []
    n = len(profits)
    for i in range(n):
        answer.append([capital[i], profits[i]])
    answer.sort(key=lambda li: li[0])
    for i in range(k):
        while cur < n and answer[cur][0] <= w:
            heapq.heappush(ans, -answer[cur][1])
            cur += 1
        if ans:
            w -= heapq.heappop(ans)
        else:
            break
    return w
