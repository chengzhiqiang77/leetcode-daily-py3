# _*_ coding = utf-8 _*_
# created by czq on 2021/11/17


# 题目318：
# 给定一个字符串数组words，找到length(word[i]) * length(word[j])的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。


# 题解1：
# 思路：遍历两次这个数组，找出最大的且没有重复字母的单词就行


def maxProduct(self, words: list[str]) -> int:
    ans = 0

    def check(str_a, str_b):
        a = 0
        b = 0
        for i in str_a:
            a += (1 << ord(i) - 97)
        for j in str_b:
            b += (1 << ord(j) - 97)
        if a & b == 0:
            return True
        else:
            return False

    for i in range(len(words)):
        for j in range(i, len(words)):
            a, b = 0, 0
            if check(set(words[i]), set(words[j])):
                ans = max(ans, len(words[i]) * len(words[j]))
    return ans
