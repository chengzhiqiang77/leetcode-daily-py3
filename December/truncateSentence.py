# _*_ coding = utf-8 _*_
# created by czq on 2021/12/10


# 题目1816：
# 句子 是一个单词列表，列表中的单词之间用单个空格隔开，且不存在前导或尾随空格。每个单词仅由大小写英文字母组成（不含标点符号）。
#
# 例如，"Hello World"、"HELLO" 和 "hello world hello world" 都是句子。
# 给你一个句子 s 和一个整数 k ，请你将 s 截断 ，使截断后的句子仅含 前 k 个单词。返回 截断 s 后得到的句子。


# 题解1：
# 思路：将s根据空格截取，然后去前k个即可；


def truncateSentence(self, s: str, k: int) -> str:
    return " ".join(s.split(" ")[i] for i in range(k))
