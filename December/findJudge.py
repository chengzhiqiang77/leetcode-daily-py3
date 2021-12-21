# _*_ coding = utf-8 _*_
# created by czq on 2021/12/21


# 题目997:
# 小镇里有 n 个人，按从 1 到 n 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。
#
# 如果小镇法官真的存在，那么：
#
# 小镇法官不会信任任何人。
# 每个人（除了小镇法官）都信任这位小镇法官。
# 只有一个人同时满足属性 1 和属性 2 。
# 给你一个数组 trust ，其中 trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人。
#
# 如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 -1 。


# 题解1：
# 思路：将这个小镇被信任的人列出来，对于这个人，列出信任他的人，对信任的人统计，当一个人被信任数量等于n-1且不信任任何人的时候，那这个人为法官；
import collections


def findJudge(self, n: int, trust: list[list[int]]) -> int:
    men, trustMen = [], []
    if n == 1:
        if not trust:
            return 1
    for i in trust:
        men.append(i[0])
        trustMen.append(i[1])
    countTrustMen = collections.Counter(trustMen)
    for i in countTrustMen:
        if countTrustMen[i] == n - 1:
            if i not in men:
                return i
    return -1
