# _*_ coding = utf-8 _*_
# created by czq on 2022/1/2


# 题目846：
# Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，并且由 groupSize 张连续的牌组成。
#
# 给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌，和一个整数 groupSize 。如果她可能重新排列这些牌，返回 true ；否则，返回 false 。


# 题解1：
# 思路：利用贪心的思想，如果在未分组的牌中，最小的数字一定是一个顺子的第一个数字，可以将hand排序，然后依次来处理；
import collections


def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
    n = len(hand)
    if n % groupSize != 0:
        return False
    hand.sort()
    ans = collections.Counter(hand)
    for i in hand:
        if ans[i] == 0:
            continue
        for j in range(i, i + groupSize):
            if ans[j] == 0:
                return False
            else:
                ans[j] -= 1
    return True
