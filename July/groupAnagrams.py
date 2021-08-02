# 题目面试题 10.02：
#
# 编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。
#
# 注意：本题相对原题稍作修改
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]


# 题解1：
# 思路：对于变位词，经过排序之后，肯定是相等的，所以可以用哈希表的方法，以排序后的词做为哈希表的键，以原来未排序的词作为值
import collections


def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    answer = collections.defaultdict(list)
    for i in strs:
        answer[''.join(sorted(i))].append(i)
    return list(answer.values())
