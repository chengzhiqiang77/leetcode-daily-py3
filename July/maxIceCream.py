# 题目1833：
# 夏日炎炎，小男孩 Tony 想买一些雪糕消消暑。
#
# 商店中新到 n 支雪糕，用长度为 n 的数组 costs 表示雪糕的定价，其中 costs[i] 表示第 i 支雪糕的现金价格。Tony 一共有 coins 现金可以用于消费，他想要买尽可能多的雪糕。
#
# 给你价格数组 costs 和现金量 coins ，请你计算并返回 Tony 用 coins 现金能够买到的雪糕的 最大数量 。
#
# 注意：Tony 可以按任意顺序购买雪糕


# 题解：该问题为经典的贪心算法问题，每个雪糕对答案的贡献都是1，优先选择价格小的物品会使得我们的剩余金额尽可能的多
def maxIceCream(self, costs: list[int], coins: int) -> int:
    count = 0
    costs = sorted(costs)
    for j in range(len(costs)):
        if costs[j] > coins:
            return count
        else:
            coins = coins - costs[j]
            count = count + 1
    return count
