# _*_ coding = utf-8 _*_
# created by czq on 2021/12/21


# 题目1518：
#
# 小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。
#
# 如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。
#
# 请你计算 最多 能喝到多少瓶酒。


# 题解1：
# 思路：将目前的空瓶先换成酒，然后继续和之前未换的一起换成酒，知道最后不再能换酒


def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    drink_num = numBottles
    while numBottles >= numExchange:
        drink = numBottles // numExchange
        drink_num += drink
        numBottles -= drink * numExchange - drink
    return drink_num
