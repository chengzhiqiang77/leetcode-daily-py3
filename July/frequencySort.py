# 题目451：
# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
#
# 示例 1:
#
# 输入:
# "tree"
#
# 输出:
# "eert"
#
# 解释:
# 'e'出现两次，'r'和't'都只出现一次。
# 因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
# ps：区分大小写

# 题解1：
# 思路：先对字符串中各字母的出现频率进行统计，然后根据出现频率进行排序，然后遍历排序后的数组，将字母按照频率次数增加到输出的字符串中
import collections


def frequencySort(self, s: str) -> str:
    strSort = ''
    m = collections.Counter(s)
    x = sorted(m.items(), key=lambda item: item[1], reverse=True)
    for i in x:
        for j in range(i[1]):
            strSort = strSort + i[0]
    return strSort