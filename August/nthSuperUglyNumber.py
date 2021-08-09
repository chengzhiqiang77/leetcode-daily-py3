# _*_ coding = utf-8 _*_
# created by czq on 2021/8/9


# 题目313：
# 超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。
#
# 给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。
#
# 题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。


# 题解1：
# 思路：要得到从小到大的第n个丑数，可以使用最小堆实现。初始时堆为空。首先将最小的丑数1加入堆。
# 每次取出堆顶元素x，则x是堆中最小的丑数，由于px也是丑数，因此将px加入堆。依次取出堆顶的元素，这个元素就是
# 第n个丑数
import heapq


def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
    visited = {1}
    heap = [1]
    for i in range(n):
        ugly = heapq.heappop(heap)
        for num in primes:
            nex = ugly * num
            if nex not in visited:
                visited.add(nex)
                heapq.heappush(heap, nex)
    return ugly

