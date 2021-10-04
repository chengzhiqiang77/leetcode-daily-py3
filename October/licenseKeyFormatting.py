# _*_ coding = utf-8 _*_
# created by czq on 2021/10/4


# 题目482：
#
# 有一个密钥字符串 S ，只包含字母，数字以及 '-'（破折号）。其中， N 个 '-' 将字符串分成了 N+1 组。
#
# 给你一个数字 K，请你重新格式化字符串，使每个分组恰好包含 K 个字符。特别地，第一个分组包含的字符个数必须小于等于 K，但至少要包含 1 个字符。
# 两个分组之间需要用 '-'（破折号）隔开，并且将所有的小写字母转换为大写字母。
#
# 给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。


# 题解1：
# 思路：对初始的字符串进行处理，然后加入"-"符号，加入的位置是每次k+余数处


def licenseKeyFormatting(self, s: str, k: int) -> str:
    res = []
    mark = 0
    answer = s.replace("-", "").upper()
    for i in answer:
        if mark != 0 and mark % k == len(answer) % k:
            res.append("-")
        res.append(i)
        mark += 1
    return "".join(res)
