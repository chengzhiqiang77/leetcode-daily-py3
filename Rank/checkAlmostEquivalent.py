# _*_ coding = utf-8 _*_
# created by czq on 2021/11/24


# 题目2068:
# 如果两个字符串 word1和 word2中从 'a'到 'z'每一个字母出现频率之差都 不超过3，那么我们称这两个字符串word1 和word2 几乎相等。
#
# 给你两个长度都为n的字符串word1 和word2，如果word1和word2几乎相等，请你返回true，否则返回false。
#
# 一个字母 x的出现 频率指的是它在字符串中出现的次数。


# 题解1：
# 思路：维护一个dict来记录word1和word2中字符的差值，遍历这个字典，当value的绝对值大于3时则返回false；
import collections


def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
    ans = collections.defaultdict(int)
    for i in range(len(word1)):
        ans[word1[i]] += 1
        ans[word2[i]] -= 1
    return all(abs(value) <= 3 for key, value in ans.items())
