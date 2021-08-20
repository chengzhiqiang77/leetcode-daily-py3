# _*_ coding = utf-8 _*_
# created by czq on 2021/8/20

# 题目541：
# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。
#
# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。


# 题解1：
# 思路：依据题意，对2k的字符串执行翻转，如果2k的字符串少于k个，则全部翻转，如果大于k个，则翻转k个，其余不变


def reverseStr(self, s: str, k: int) -> str:
    s = list(s)
    n = len(s)
    for i in range(0, n, 2 * k):
        s[i:i + k] = reversed(s[i:i + k])
    return "".join(s)
