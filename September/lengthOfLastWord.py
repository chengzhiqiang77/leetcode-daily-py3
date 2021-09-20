# _*_ coding = utf-8 _*_
# created by czq on 2021/9/21


# 题目58：
# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。
#
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。


# 题解1：
# 思路：反向遍历，直接遍历最后一个单词，然后返回其长度即可


def lengthOfLastWord(self, s: str) -> int:
    str_last_len = 0
    s_length = len(s) - 1
    while s[s_length] == " ":
        s_length -= 1
    while s[s_length] != " " and s_length > -1:
        s_length -= 1
        str_last_len += 1
    return str_last_len


# 题解2：
# 思路：正向遍历，遍历到最后一个单词，记录其长度即可

def lengthOfLastWord(self, s: str) -> int:
    str_len, str_last_len = 0, 0
    for i in range(len(s)):
        if s[i] != " ":
            str_len += 1
        elif str_len > 0:
            str_last_len = str_len
            str_len = 0
    return str_last_len if str_len == 0 else str_len
