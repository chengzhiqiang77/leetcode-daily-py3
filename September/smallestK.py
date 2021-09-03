# _*_ coding = utf-8 _*_
# created by czq on 2021/9/3


# 题目面试题17.14：
# 设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。


# 题解1：
# 思路：将数组排序，输出前面k个即可
import heapq


def smallestK(self, arr: list[int], k: int) -> list[int]:
    return sorted(arr)[:k]


# 题解2：
# 思路：这是个典型的topk问题，可使用小根堆来求解


def smallestK(self, arr: list[int], k: int) -> list[int]:
    heapq.heapify(arr)
    answer = []
    for i in range(k):
        answer.append(heapq.heappop(arr))
    return answer
