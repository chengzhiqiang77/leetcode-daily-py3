# _*_ coding = utf-8 _*_
# created by czq on 2021/11/29


# 题目438：
# 给定两个字符串s和 p，找到s中所有p的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。


# 题解1：
# 思路：遍历s，对其中符合异位词的输出即可；
import collections


def findAnagrams(self, s: str, p: str):
    len_p = len(p)
    nums_p = collections.Counter(p)
    ans = []
    for key, value in enumerate(s):
        if collections.Counter(s[key:key + len_p]) == nums_p:
            ans.append(key)
    return ans
