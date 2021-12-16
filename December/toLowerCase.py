# _*_ coding = utf-8 _*_
# created by czq on 2021/12/16


# 题目709：
# 给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。


# 题解1：
# 思路：使用lower()方法直接转换即可；


def toLowerCase(self, s: str) -> str:
    return s.lower()
