# _*_ coding = utf-8 _*_
# created by czq on 2021/11/23


# 题目859：
#
# 给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回 true ；否则返回 false 。
#
# 交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。
#
# 例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。


# 题解1：
# 思路：当两个字符串的长度不一样时，不符合题目要求；当字符串长度一样时，如果两个字符串中仅有两个元素不一样，且两个元素相等，则符合题目要求；
# 还有一种情况时两个字符串相同时，且字符串中出现最多的元素大于等于两次即可；
import collections


def buddyStrings(self, s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    count_s = collections.Counter(s)
    ans = []
    num = 0
    for i in range(len(s)):
        if s[i] != goal[i]:
            num += 1
            ans.append(i)
        if num > 2:
            return False
    if num == 2 and s[ans[0]] == goal[ans[1]] and s[ans[1]] == goal[ans[0]]:
        return True
    elif num == 0:
        count_s = collections.Counter(s)
        for key, value in count_s.items():
            if value >= 2:
                return True
        else:
            return False
    else:
        return False
