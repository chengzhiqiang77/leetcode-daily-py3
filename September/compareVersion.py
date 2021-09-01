# _*_ coding = utf-8 _*_
# created by czq on 2021/9/1


# 题目165：
# 给你两个版本号 version1 和 version2 ，请你比较它们。
#
# 版本号由一个或多个修订号组成，各修订号由一个 '.' 连接。每个修订号由 多位数字 组成，可能包含 前导零 。每个版本号至少包含一个字符。
# 修订号从左到右编号，下标从 0 开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，以此类推。例如，2.5.33 和 0.1 都是有效的版本号。
#
# 比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 忽略任何前导零后的整数值 。也就是说，修订号 1 和修订号 001 相等 。
# 如果版本号没有指定某个下标处的修订号，则该修订号视为 0 。例如，版本 1.0 小于版本 1.1 ，因为它们下标为 0 的修订号相同，而下标为 1
# 的修订号分别为 0 和 1 ，0 < 1 。
#
# 返回规则如下：
#
# 如果version1>version2返回1，
# 如果version1<version2 返回 -1，
# 除此之外返回 0。


# 题解1：
# 思路：定义两个指针，分别向后处理字符串，比较版本号


def compareVersion(self, version1: str, version2: str) -> int:
    n, m = len(version1), len(version2)
    i, j = 0, 0

    while i < n or j < m:
        x = y = 0
        while i < n and version1[i] != ".":
            x = x * 10 + int(version1[i])
            i += 1
        while j < m and version2[j] != ".":
            y = y * 10 + int(version2[j])
            j += 1
        j += 1
        i += 1
        if x != y:
            return 1 if x > y else -1
    return 0
