# _*_ coding = utf-8 _*_
# created by czq on 2021/10/9


# 题目352：
#  给你一个由非负整数a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。
#
# 实现 SummaryRanges 类：
#
# SummaryRanges() 使用一个空数据流初始化对象。
# void addNum(int val) 向数据流中加入整数 val 。
# int[][] getIntervals() 以不相交区间[starti, endi] 的列表形式返回对数据流中整数的总结。


# 题解1：
# 思路：在数据流中加入整数的时候，可以先去重，然后在计算不相交区间时，转为list然后排序，排序后遍历这个有序的数组，然后输出即可


class SummaryRanges:

    def __init__(self):
        self.val_list = set()

    def addNum(self, val: int) -> None:
        self.val_list.add(val)

    def getIntervals(self) -> list[list[int]]:
        _val_list1 = list(self.val_list)
        _val_list1.sort()
        i = 0
        val_length = len(_val_list1)
        res = []
        while i < val_length:
            begin = _val_list1[i]
            end = begin
            while i < val_length - 1 and _val_list1[i + 1] == _val_list1[i] + 1:
                end = _val_list1[i + 1]
                i += 1
            res.append([begin, end])
            i += 1
        return res
