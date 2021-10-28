# _*_ coding = utf-8 _*_
# created by czq on 2021/10/28


# 题目869：
# 给定正整数 N，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
#
# 如果我们可以通过上述方式得到2 的幂，返回 true；否则，返回 false。


# 题解1：
# 思路：统计N中每一个数字出现的频率，如果该字典与统计同样位数的2的幂数的字典是一样的，则返回True，反之返回False
import collections


def reorderedPowerOf2(self, n: int) -> bool:
    ans, number = {}, 1
    for i in range(1, 11):
        ans[i] = []
    while number <= 10 ** 9:
        ans[len(str(number))].append(number)
        number *= 2
    n_length = len(str(n))
    for nu in ans[n_length]:
        if collections.Counter(str(nu)) == collections.Counter(str(n)):
            return True
    return False
