# _*_ coding = utf-8 _*_
# created by czq on 2021/10/7


# 题目434：
# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
#
# 请注意，你可以假定字符串里不包括任何不可打印的字符。


# 题解1：
# 思路：根据题目的描述，我们可以只记录单词开始的计入计数即可；


def countSegments(self, s: str) -> int:
    res = 0
    for num in range(len(s)):
        if (num == 0 or s[num - 1] == " ") and s[num] != " ":
            res += 1
    return res
