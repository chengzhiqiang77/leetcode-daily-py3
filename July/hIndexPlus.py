# 题目275：
#
# 给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照升序排列 。编写一个方法，计算出研究者的h指数。
#
# h指数的定义: “h代表“高引用次数”（highcitations），一名科研人员的h指数是指他（她）的 （N篇论文中）总共有h篇论文分别被引用了至少h次。（其余的
# N - h篇论文每篇被引用次数不多于h次。）"
#
# 示例:
#
# 输入: citations = [0, 1, 3, 5, 6]
# 输出: 3
# 解释: 给定数组表示研究者总共有
# 5篇论文，每篇论文相应的被引用了0, 1, 3, 5, 6次。由于研究者有3篇论文每篇至少被引用了3次，其余两篇论文每篇被引用不多于3次，所以她的h
# 指数是3。

# 题解1：
# 思路：h指数肯定有以下特性：对于小于h的值，都满足h指数的特性，只需要遍历，找到最后一个满足h指数特性的数字即可


def hIndex(self, citations: list[int]) -> int:
    # citations = sorted(citations, reverse=True)
    n = len(citations)
    i = 1
    if citations[n - 1] == 0:
        return 0
    if n == 1:
        return 1
    for i in range(n):
        if i == n - 1:
            return i + 1
        if i + 1 <= citations[-(i + 1)] and i + 2 > citations[-(i + 2)]:
            return i + 1