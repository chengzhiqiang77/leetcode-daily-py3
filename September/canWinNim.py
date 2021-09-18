# _*_ coding = utf-8 _*_
# created by czq on 2021/9/18


# 题目292：
# 你和你的朋友，两个人一起玩Nim 游戏：
#
# 桌子上有一堆石头。
# 你们轮流进行自己的回合，你作为先手。
# 每一回合，轮到的人拿掉1 - 3 块石头。
# 拿掉最后一块石头的人就是获胜者。
# 假设你们每一步都是最优解。请编写一个函数，来判断你是否可以在给定石头数量为 n 的情况下赢得游戏。如果可以赢，返回 true；否则，返回 false 。


# 题解1：
# 思路：要想赢得游戏，只需要在我们那的时候，把剩下的石头数量拿成四的倍数，这样我们就可以在被别人拿走后，拿上4-n个，从而赢得游戏


def canWinNim(self, n: int) -> bool:
    return n % 4 != 0
