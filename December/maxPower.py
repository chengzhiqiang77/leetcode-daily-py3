# _*_ coding = utf-8 _*_
# created by czq on 2021/12/4


# 题目1446：
# 给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。
#
# 请你返回字符串的能量。


# 题解1：
# 思路：遍历一次这个字符串，记录当前字符出现的个数，并与最大出现数字比较


def maxPower(self, s: str) -> int:
    max_num = 0
    num = 0
    tmp = ""
    for i in s:
        if i != tmp:
            tmp = i
            max_num = max(num, max_num)
            num = 1
        else:
            num += 1
    return max(max_num, num)
