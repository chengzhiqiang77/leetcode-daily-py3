# _*_ coding = utf-8 _*_
# created by czq on 2021/8/31


# 题目1109：
# 这里有n个航班，它们分别从 1 到 n 进行编号。
#
# 有一份航班预订表bookings ，表中第i条预订记录bookings[i] = [firsti, lasti, seatsi]意味着在从 firsti到 lasti
# （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi个座位。
#
# 请你返回一个长度为 n 的数组answer，其中 answer[i] 是航班 i 上预订的座位总数。


# 题解1：
# 思路：对于给定的bookings，可以求出answer数列的差分数列，对差分数列进行求前缀和，前缀和数组即为answer
import itertools


def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
    diff = [0 for i in range(n)]
    for first, last, seats in bookings:
        diff[first - 1] += seats
        if last < n:
            diff[last] -= seats
    return list(itertools.accumulate(diff))
