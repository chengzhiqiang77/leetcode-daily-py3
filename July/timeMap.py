# 题目981：
# 创建一个基于时间的键值存储类TimeMap，它支持下面两个操作：
#
# 1. set(string key, string value, int timestamp)
#
# 存储键key、值value，以及给定的时间戳timestamp。
# 2. get(string key, int timestamp)
#
# 返回先前调用set(key, value, timestamp_prev)所存储的值，其中timestamp_prev <= timestamp。
# 如果有多个这样的值，则返回对应最大的  timestamp_prev的那个值。
# 如果没有值，则返回空字符串（""）。
#
# 示例 1：
#
# 输入：inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],
# ["foo","bar2",4],["foo",4],["foo",5]]
# 输出：[null,null,"bar","bar",null,"bar2","bar2"]
# 解释：
# TimeMap kv;
# kv.set("foo", "bar", 1); // 存储键 "foo" 和值 "bar" 以及时间戳 timestamp = 1
# kv.get("foo", 1);  // 输出 "bar"
# kv.get("foo", 3); // 输出 "bar" 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"）
# kv.set("foo", "bar2", 4);
# kv.get("foo", 4); // 输出 "bar2"
# kv.get("foo", 5); // 输出 "bar2"

# 题解1：
# 思路：利用一个多重字典存储，然后通过key找出相应的字典，遍历字典，找出最大的值
import collections


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tables = collections.defaultdict(collections.Counter)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tables[key][value] = timestamp

    def get(self, key: str, timestamp: int) -> str:
        m = self.tables[key]
        n = -1
        answer = 0
        for key1, value in m.items():
            if value <= timestamp:
                if value > n:
                    n = value
                    answer = key1
        return (n != -1) and answer or ''
