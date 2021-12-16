# _*_ coding = utf-8 _*_
# created by czq on 2021/12/16


# 题目748：
# 给你一个字符串 licensePlate 和一个字符串数组 words ，请你找出并返回 words 中的 最短补全词 。
#
# 补全词 是一个包含 licensePlate 中所有字母的单词。
#
# 在匹配 licensePlate 中的字母时：
#
# 忽略licensePlate 中的 数字和空格 。
# 不区分大小写。
# 如果某个字母在 licensePlate 中出现不止一次，那么该字母在补全词中的出现次数应当一致或者更多。
# 例如：licensePlate = "aBc 12c"，那么它的补全词应当包含字母 'a'、'b' （忽略大写）和两个 'c' 。可能的 补全词 有 "abccdef"、"caaacab" 以及 "cbca" 。
#
# 请你找出并返回 words 中的 最短补全词 。题目数据保证一定存在一个最短补全词。当有多个单词都符合最短补全词的匹配条件时取 words 中 第一个 出现的那个。


# 题解1：
# 思路：找出licensePlate中有的字母，然后匹配words中的，取出其中符合条件的最短单词即可；
import collections
from math import inf


def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
    ans = collections.Counter(i.lower() for i in licensePlate if i.isalpha())
    min_num = inf
    min_pla = inf
    for key, i in enumerate(words):
        res = collections.Counter(i)
        for j in ans:
            if res[j] < ans[j]:
                break
        else:
            if min_num > len(i):
                min_num = len(i)
                min_pla = key
    return words[min_pla]
