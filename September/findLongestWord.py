# _*_ coding = utf-8 _*_
# created by czq on 2021/9/14


# 题目524:
# 给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
#
# 如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。


# 题解1：
# 思路：我们可以先把字符串数组先按照数组内字符串的长度排序，如果字符串长度一样，则按照字典序排序，得到排序后的数组，我们只需要遍历数组，
# 如果字符串符合题目的要求，直接return字符串即可；而对于寻找字符串的算法实现，我们可以使用双指针，一个指向字符串s的初始位置，
# 一个指向字符串数组中字符串的初始位置，当在字符串中找到一个匹配s的字母时，将两个指针同时往后移动，如果没找到，则只移动在字符串数组中字符串的指针，
# 最后遍历完后，如果s中的指针指向了最后一个字符后面的位置，则认为当前字符串符合要求；


def findLongestWord(self, s: str, dictionary: list[str]) -> str:
    dictionary.sort(key=lambda x: (-len(x), x))
    for word in dictionary:
        i, j = 0, 0
        while i < len(s) and j < len(word):
            if word[j] == s[i]:
                j += 1
            i += 1
        if j == len(word):
            return word
    return ""
