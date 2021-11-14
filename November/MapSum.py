# _*_ coding = utf-8 _*_
# created by czq on 2021/11/14


# 题目677：
# 实现一个 MapSum 类，支持两个方法，insert和sum：
#
# MapSum() 初始化 MapSum 对象
# void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。
# int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。


# 题解1：
# 思路：对于查找value的时候，使用切片来匹配value，计算出总和
import collections


class MapSum:

    def __init__(self):
        self.dict = collections.Counter()

    def insert(self, key: str, val: int) -> None:
        self.dict[key] = val

    def sum(self, prefix: str) -> int:
        n = len(prefix)
        sum = 0
        for key, value in self.dict.items():
            if key[0: n] == prefix:
                sum += value
        return sum
