# _*_ coding = utf-8 _*_
# created by czq on 2021/10/8


# 题目187：
# 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。
# 在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
#
# 编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。


# 题解1：
# 思路：遍历这个字符串，用一个哈希表记录各个DNA出现的个数，找出大于0的即可；在实际运算中，我们可以只遍历一遍，然后在这个DNA出现次数到达2的时候，就
# 可以加入到答案中，后续不需要继续处理
import collections


def findRepeatedDnaSequences(self, s: str) -> list[str]:
    ans = collections.Counter()
    res = []
    for i in range(len(s) - 9):
        ans[s[i:i + 10]] += 1
        if ans[s[i:i + 10]] == 2:
            res.append(s[i:i + 10])
    return res
