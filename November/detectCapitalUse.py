# _*_ coding = utf-8 _*_
# created by czq on 2021/11/14


# 题目520：
# 我们定义，在以下情况时，单词的大写用法是正确的：
#
# 全部字母都是大写，比如 "USA" 。
# 单词中所有字母都不是大写，比如 "leetcode" 。
# 如果单词不只含有一个字母，只有首字母大写，比如"Google" 。
# 给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。


# 题解1：
# 思路：简单的字符串模拟题，按照题目要求判断即可


def detectCapitalUse(self, word: str) -> bool:
    return word.isupper() or word.islower() or word.istitle()
