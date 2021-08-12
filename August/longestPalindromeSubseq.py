# _*_ coding = utf-8 _*_
# created by czq on 2021/8/12


# 题目516：
# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
#
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。


# 题解1：
# 思路：回文字符串的定义为：该字符串正着读反着读都一样，则我们可以得到一个式子，用i表示第一个元素，j表示最后一个元素，则s[i] = s[j],单个字母是一个
# 最短的回文字符串，我么用dp[i][j]表示i～j的最大回文子序列，则当s[i] = s[j]时，dp[i][j] = dp[i+1][j-1] + 2,当s[i] != s[j]，dp[i][j]=
# max(dp[i+1][j], dp[i][j-1])


def longestPalindromeSubseq(self, s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]

