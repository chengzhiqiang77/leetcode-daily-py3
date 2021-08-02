# 题目1846：给你一个正整数数组arr。请你对 arr执行一些操作（也可以不进行任何操作），使得数组满足以下条件：
#
# arr中 第一个元素必须为1。
# 任意相邻两个元素的差的绝对值 小于等于1，也就是说，对于任意的 1 <= i < arr.length（数组下标从 0 开始），
# 都满足abs(arr[i] - arr[i - 1]) <= 1。abs(x)为x的绝对值。
# 你可以执行以下 2 种操作任意次：
#
# 减小 arr中任意元素的值，使其变为一个 更小的正整数。
# 重新排列arr中的元素，你可以以任意顺序重新排列。


# 题解1：
# 思路：由于对排序后数组做的操作，只能使得arr中的元素变小，所以n的最大值为len(arr),故我们只需要遍历arr，然后取arr[i]和n的最小值即可


def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
    answer = 1
    arr = sorted(arr)
    for num in arr[1:]:
        answer = min(answer + 1, num)
    return answer
