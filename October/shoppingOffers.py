# _*_ coding = utf-8 _*_
# created by czq on 2021/10/24


# 题目638：
#
# 在 LeetCode 商店中， 有 n 件在售的物品。每件物品都有对应的价格。然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。
#
# 给你一个整数数组 price 表示物品价格，其中 price[i] 是第 i 件物品的价格。另有一个整数数组 needs 表示购物清单，其中 needs[i] 是需要购买第 i 件物品的数量。
#
# 还有一个数组 special 表示大礼包，special[i] 的长度为 n + 1 ，其中 special[i][j] 表示第 i 个大礼包中内含第 j 件物品的数量，且 special[i][n] （也就是数组中的最后一个整数）为第 i 个大礼包的价格。
#
# 返回 确切 满足购物清单所需花费的最低价格，你可以充分利用大礼包的优惠活动。你不能购买超出购物清单指定数量的物品，即使那样会降低整体价格。任意大礼包可无限次购买。


# 题解1：
# 思路：要最省钱的方案，我们可以先吧礼包中大于单买的给去除，然后求出所有的可能的方案，求出最小值


def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
    n = len(price)
    cheap_list = []
    for goods in special:
        if sum(goods[i] for i in range(n)) > 0 and sum(goods[i] * price[i] for i in range(n)) > goods[-1]:
            cheap_list.append(goods)

    def dfs(cur_needs):
        # 不购买任何大礼包，原价购买购物清单中的所有物品
        min_price = sum(need * price[i] for i, need in enumerate(cur_needs))
        for cur_special in cheap_list:
            special_price = cur_special[-1]
            nxt_needs = []
            for i in range(n):
                if cur_special[i] > cur_needs[i]:  # 不能购买超出购物清单指定数量的物品
                    break
                nxt_needs.append(cur_needs[i] - cur_special[i])
            if len(nxt_needs) == n:  # 大礼包可以购买
                min_price = min(min_price, dfs(tuple(nxt_needs)) + special_price)
        return min_price

    return dfs(tuple(needs))
