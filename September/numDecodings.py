# _*_ coding = utf-8 _*_
# created by czq on 2021/9/27


# 题目639：
# 一条包含字母A-Z 的消息通过以下的方式进行了编码：
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 要 解码 一条已编码的消息，所有的数字都必须分组，然后按原来的编码方案反向映射回字母（可能存在多种方式）。例如，"11106" 可以映射为：
#
# "AAJF" 对应分组 (1 1 10 6)
# "KJF" 对应分组 (11 10 6)
# 注意，像 (1 11 06) 这样的分组是无效的，因为 "06" 不可以映射为 'F' ，因为 "6" 与 "06" 不同。
#
# 除了 上面描述的数字字母映射方案，编码消息中可能包含 '*' 字符，可以表示从 '1' 到 '9' 的任一数字（不包括 '0'）。例如，编码字符串 "1*"
# 可以表示 "11"、"12"、"13"、"14"、"15"、"16"、"17"、"18" 或 "19" 中的任意一条消息。对 "1*" 进行解码，
# 相当于解码该字符串可以表示的任何编码消息。
#
# 给你一个字符串 s ，由数字和 '*' 字符组成，返回 解码 该字符串的方法 数目 。
#
# 由于答案数目可能非常大，返回对 109 + 7 取余 的结果。


# 题解1：
# 思路：这个题目和之前的解码方法是一样的，但是不同的是加入了"*"这个概念，在写出状态转移方程的时候，需要考虑到*的状态转移；

def numDecodings(self, s: str) -> int:
    n = len(s)
    mod = 10 ** 9 + 7
    f = [1] + [0] * n

    def digit1(string):
        if string == "0":
            return 0
        return 9 if string == "*" else 1

    def digit2(string):
        if string[0] == "*":
            if string[1] == "*":
                return 15
            return 2 if 0 <= int(string[1]) <= 6 else 1
        if string[1] == "*":
            if string[0] == "1":
                return 9
            return 6 if string[0] == "2" else 0
        if "*" not in string:
            return 1 if string[0] != "0" and int(string) <= 26 else 0

    for i in range(1, n + 1):
        f[i] += (f[i - 1] * digit1(s[i - 1])) % mod
        f[i] = f[i] + ((f[i - 2] * digit2(s[i - 2:i])) % mod) if i > 1 else f[i]
    return f[n] % mod
