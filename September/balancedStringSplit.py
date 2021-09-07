# _*_ coding = utf-8 _*_
# created by czq on 2021/9/7


# 题目1221：
# 在一个 平衡字符串 中，'L' 和 'R' 字符的数量是相同的。
#
# 给你一个平衡字符串s，请你将它分割成尽可能多的平衡字符串。
#
# 注意：分割得到的每个字符串都必须是平衡字符串。
#
# 返回可以通过分割得到的平衡字符串的 最大数量 。


# 题解1：
# 思路：我们可以对s进行遍历，找出平衡字符串后继续进行遍历，由于s为一个平衡字符串，剩余部分也为一个平衡字符串，我们可以继续遍历，我们可以将L看作1，
# R看作-1，平衡字符串就是字符中所有值相加为0


def balancedStringSplit(self, s: str) -> int:
    answer, target = 0, 0
    for i in s:
        if i == "R":
            target += 1
        else:
            target -= 1
        if not target:
            answer += 1
    return answer
