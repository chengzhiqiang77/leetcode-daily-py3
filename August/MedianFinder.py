# _*_ coding = utf-8 _*_
# created by czq on 2021/8/27


# 题目295：
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
#
# 例如，
#
# [2,3,4]的中位数是 3
#
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
#
# 设计一个支持以下两种操作的数据结构：
#
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。


# 题解1：
# 思路：根据题意设计，addNum函数往列表中执行append操作，findMedian排序后进行判断执行


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.li = list()

    def addNum(self, num: int) -> None:
        self.li.append(num)

    def findMedian(self) -> float:
        _li = self.li
        _li.sort()
        return (_li[int(len(_li) / 2 - 1)] + _li[int(len(_li) / 2)]) / 2 if len(_li) % 2 == 0 else _li[
            int(len(_li) / 2)]
