# _*_ coding = utf-8 _*_
# created by czq on 2021/9/29


# 题目517：
#
# 假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。
#
# 在每一步操作中，你可以选择任意 m (1 <= m <= n) 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。
#
# 给定一个整数数组 machines 代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的 最少的操作步数 。
# 如果不能使每台洗衣机中衣物的数量相等，则返回 -1 。


# 题解1：
# 思路：如果衣服总数不能被洗衣机个数整除，则不能使每台洗衣机的衣物相等，我们可以求出每台洗衣机离目标衣物还差多少，由于每次可以给多台洗衣机送衣服，
# 但是每次一台洗衣机只能送一次衣服，所以数量大于目标衣物的至少都要送差值的数目，然后负数的只需要从前面的洗衣机处依次往回运就行


def findMinMoves(self, machines: list[int]) -> int:
    if sum(machines) % len(machines):
        return -1
    avg = sum(machines) // len(machines)
    sum1 = 0
    answer = 0
    for i in machines:
        i -= avg
        sum1 += i
        answer = max(abs(sum1), i, answer)
    return answer
