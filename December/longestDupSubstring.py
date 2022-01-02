# _*_ coding = utf-8 _*_
# created by czq on 2022/1/2


# 题目1044：
# 给你一个字符串 s ，考虑其所有 重复子串 ：即，s 的连续子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。
#
# 返回 任意一个 具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。


# 题解1：
# 思路：利用动态规划，由于最后求的是最长的重复字串，所以最长的重复子串的子串也是具有重复子串的性质；所以我们可以便利这个字符串来找出答案；


def longestDupSubstring(self, s: str) -> str:
    ans = ""
    for i in range(len(s)):
        while s[i:i + len(ans) + 1] in s[i + 1:]:
            ans = s[i:i + len(ans) + 1]
    return ans
