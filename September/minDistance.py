# _*_ coding = utf-8 _*_
# created by czq on 2021/9/25


# 题目583：
# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。


# 题解1：
# 思路：对于word1和word2，每一步可以删除单词中的字母，我们只需要找出word1和word2中最长的公共子序列即可，答案就是
# word1的长度减去子序列的长度加上word2的长度减去子序列的长度；


def minDistance(self, word1: str, word2: str) -> int:
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return len(word1) + len(word2) - dp[-1][-1] * 2
