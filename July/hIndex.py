# 题目274：
# 给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h指数。
#
# h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。
# 且其余的N - h篇论文每篇被引用次数不超过 h 次。
#
# 例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。
#
#
# 示例：
#
# 输入：citations = [3,0,6,1,5]
# 输出：3
# 解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
#    由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。

# 题解1：
# 思路：h指数肯定有以下特性：对于小于h的值，都满足h指数的特性，只需要遍历，找到最后一个满足h指数特性的数字即可


def hIndex(self, citations: list[int]) -> int:
    citations = sorted(citations, reverse=True)
    n = len(citations)
    i = 1
    if citations[0] == 0:
        return 0
    if n == 1:
        return 1
    for i in range(n):
        if i == n - 1:
            return i + 1
        if i + 1 <= citations[i] and i + 2 > citations[i + 1]:
            return i + 1