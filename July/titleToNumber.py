# _*_ coding = utf-8 _*_
# created by czq on 2021/7/30


# 题目171：
# 给你一个字符串columnTitle ，表示 Excel 表格中的列名称。返回该列名称对应的列序号。
#
#
# 例如，
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...


# 题解1：
# 思路：这道题目其实是求字母的ascll码，且该字母为26进制


def titleToNumber(self, columnTitle: str) -> int:
    answer = 0
    for c in columnTitle:
        cur = ord(c) - ord('A') + 1
        answer = answer * 26 + cur
    return answer
