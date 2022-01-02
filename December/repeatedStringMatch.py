# _*_ coding = utf-8 _*_
# created by czq on 2022/1/2


# 题目686：
# 给定两个字符串a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。
#
# 注意：字符串 "abc"重复叠加 0 次是 ""，重复叠加 1 次是"abc"，重复叠加 2 次是"abcabc"。


# 题解1：
# 思路：可以计算出字符串b的长度是字符串a的长度的倍数，得到倍数target，如果答案存在，只有三种情况：target,target+1,target+2；所以，我们只需要
# 枚举这三种情况即可；


def repeatedStringMatch(self, a: str, b: str) -> int:
    a_len = len(a)
    b_len = len(b)
    target = b_len // a_len
    one_nums = a * target
    two_nums = a * (target + 1)
    three_nums = a * (target + 2)
    if b in one_nums:
        return target
    elif b in two_nums:
        return target + 1
    elif b in three_nums:
        return target + 2
    else:
        return -1
