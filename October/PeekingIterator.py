# _*_ coding = utf-8 _*_
# created by czq on 2021/10/7


# 题目284：
# 请你设计一个迭代器，除了支持 hasNext 和 next 操作外，还支持 peek 操作。
#
# 实现 PeekingIterator 类：
#
# PeekingIterator(int[] nums) 使用指定整数数组 nums 初始化迭代器。
# int next() 返回数组中的下一个元素，并将指针移动到下个元素处。
# bool hasNext() 如果数组中存在下一个元素，返回 true ；否则，返回 false 。
# int peek() 返回数组中的下一个元素，但 不 移动指针。


# 题解1：
# 思路：根据题意实现即可


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.pk = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.pk:
            self.pk = self.iterator.next()
        return self.pk

    def next(self):
        """
        :rtype: int
        """
        if self.pk:
            val = self.pk
            self.pk = None
            return val
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pk is not None or self.iterator.hasNext()
