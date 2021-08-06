# _*_ coding = utf-8 _*_
# created by czq on 2021/8/6
import collections


# 题目242：
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 注意：若s 和 t中每个字符出现的次数都相同，则称s 和 t互为字母异位词。


# 题解1：
# 思路：将两个字符串排序后，如果相等的话，则输出True，反之输出False


def isAnagram(self, s: str, t: str) -> bool:
    return sorted(list(s)) == sorted((list(t)))


# 题解1：
# 思路：利用哈希表（字典）统计字符串中每个字母出现的次数，如果两个字典相同，则返回True，反之则返回False


def isAnagram(self, s: str, t: str) -> bool:
    return collections.Counter(s) == collections.Counter(t)
