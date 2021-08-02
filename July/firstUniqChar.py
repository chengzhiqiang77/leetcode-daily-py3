# 题目387：
#   给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
import collections


# 题解1：
def firstUniqChar(self, s):
    m = {}
    for word in s:
        m[word] = 0
    for word in s:
        m[word] += 1
    for key, value in m.items():
        if value == 1:
            return s.index(key)
    return -1


# 题解2：
def firstUniqChar(self, s):
    frequency = collections.Counter(s)
    for i, ch in enumerate(s):
        if frequency[ch] == 1:
            return i
    return -1


# 题解3：
def firstUniqChar(self, s):
    position = dict()
    n = len(s)
    for i, ch in enumerate(s):
        if ch in position:
            position[ch] = -1
        else:
            position[ch] = i
    for pos in position.values():
        if pos != -1:
            return pos
    return -1
