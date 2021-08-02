# 题目997：
# 在一个小镇里，按从 1 到 n 为 n 个人进行编号。传言称，这些人中有一个是小镇上的秘密法官。
#
# 如果小镇的法官真的存在，那么：
#
# 小镇的法官不相信任何人。
# 每个人（除了小镇法官外）都信任小镇的法官。
# 只有一个人同时满足条件 1 和条件 2 。
# 给定数组trust，该数组由信任对 trust[i] = [a, b]组成，表示编号为 a 的人信任编号为 b 的人。
#
# 如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的编号。否则，返回 -1。
#
#  
#
# 示例 1：
#
# 输入：n = 2, trust = [[1,2]]
# 输出：2
# 示例 2：
#
# 输入：n = 3, trust = [[1,3],[2,3]]
# 输出：3
# 示例 3：
#
# 输入：n = 3, trust = [[1,3],[2,3],[3,1]]
# 输出：-1
# 示例 4：
#
# 输入：n = 3, trust = [[1,2],[2,3]]
# 输出：-1
# 示例 5：
#
# 输入：n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# 输出：3

# 题解1：
# 思路：根据题意可得，小镇法官拥有以下几个特性：不相信任何人，除了自己都信任小镇法官；可以得出，在trust中，不会出现小镇法官信任别人的情况，
# 而且所有信任的小镇法官的人为n-1；
import collections


def findJudge(self, n: int, trust: list[list[int]]) -> int:
    men, trust_men = [], []
    if n == 1:
        if not trust:
            return 1
    for i in trust:
        men.append(i[0])
        trust_men.append(i[1])
    count_trust_men = collections.Counter(trust_men)
    for i in count_trust_men:
        if count_trust_men[i] == n - 1:
            if i not in men:
                return i
    return -1
