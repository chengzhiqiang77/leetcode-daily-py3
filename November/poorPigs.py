# _*_ coding = utf-8 _*_
# created by czq on 2021/11/29


# 题目458：
# 有 buckets 桶液体，其中 正好 有一桶含有毒药，其余装的都是水。它们从外观看起来都一样。为了弄清楚哪只水桶含有毒药，你可以喂一些猪喝，通过观察猪是否会死进行判断。不幸的是，你只有 minutesToTest 分钟时间来确定哪桶液体是有毒的。
#
# 喂猪的规则如下：
#
# 选择若干活猪进行喂养
# 可以允许小猪同时饮用任意数量的桶中的水，并且该过程不需要时间。
# 小猪喝完水后，必须有 minutesToDie 分钟的冷却时间。在这段时间里，你只能观察，而不允许继续喂猪。
# 过了 minutesToDie 分钟后，所有喝到毒药的猪都会死去，其他所有猪都会活下来。
# 重复这一过程，直到时间用完。
# 给你桶的数目 buckets ，minutesToDie 和 minutesToTest ，返回在规定时间内判断哪个桶有毒所需的 最小 猪数。


# 题解1：
# 思路：看题解，利用香农熵原理（自己做不来！！）


def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    pigs = 0
    while (minutesToTest // minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs

