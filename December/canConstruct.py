# _*_ coding = utf-8 _*_
# created by czq on 2021/12/4


# 题目383：
# 为了不在赎金信中暴露字迹，从杂志上搜索各个需要的字母，组成单词来表达意思。
#
# 给你一个赎金信 (ransomNote) 字符串和一个杂志(magazine)字符串，判断 ransomNote 能不能由 magazines 里面的字符构成。
#
# 如果可以构成，返回 true ；否则返回 false 。
#
# magazine 中的每个字符只能在 ransomNote 中使用一次。


# 题解1：
# 思路：利用哈希表记录两个字符串字符出现的次数，依次比较即可
import collections


def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    maga_dict = collections.Counter(magazine)
    for i in ransomNote:
        if maga_dict[i]:
            maga_dict[i] -= 1
        else:
            return False
    return True
