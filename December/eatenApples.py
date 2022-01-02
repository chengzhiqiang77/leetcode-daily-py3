# _*_ coding = utf-8 _*_
# created by czq on 2022/1/2


# 题目1705：
# 有一棵特殊的苹果树，一连 n 天，每天都可以长出若干个苹果。在第 i 天，树上会长出 apples[i] 个苹果，这些苹果将会在 days[i] 天后（也就是说，第 i + days[i] 天时）腐烂，变得无法食用。也可能有那么几天，树上不会长出新的苹果，此时用 apples[i] == 0 且 days[i] == 0 表示。
#
# 你打算每天 最多 吃一个苹果来保证营养均衡。注意，你可以在这 n 天之后继续吃苹果。
#
# 给你两个长度为 n 的整数数组 days 和 apples ，返回你可以吃掉的苹果的最大数目。


# 题解1：
# 思路：利用贪心的思想，当天吃掉的是距离当天最快腐烂的苹果（和家里的奶奶一样～），具体实现使用一个最小堆，维护距离当前日期最近的腐烂日期；
import heapq


def eatenApples(self, apples: list[int], days: list[int]) -> int:
    pq, i, ans = [], 0, 0
    while i < len(apples) or pq:
        while pq and pq[0][0] <= i:
            heapq.heappop(pq)
        if i < len(apples) and apples[i]:
            heapq.heappush(pq, [i + days[i], apples[i]])
        if pq:
            pq[0][1] -= 1
            ans += 1
            if not pq[0][1]:
                heapq.heappop(pq)
        i += 1
    return ans
