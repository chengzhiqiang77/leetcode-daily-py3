# _*_ coding = utf-8 _*_
# created by czq on 2021/10/18


# 题目476：
# 对整数的二进制表示取反（0 变 1 ，1 变 0）后，再转换为十进制表示，可以得到这个整数的补数。
#
# 例如，整数 5 的二进制表示是 "101" ，取反后得到 "010" ，再转回十进制表示得到补数 2 。
# 给你一个整数 num ，输出它的补数。


# 题解1：
# 思路：将整数的每一位都与1取异或即可


def findComplement(self, num: int) -> int:
    pows = len(str(bin(num))) - 2
    ans = (2 ** pows) - 1
    return num ^ ans