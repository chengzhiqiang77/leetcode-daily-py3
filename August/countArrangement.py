# _*_ coding = utf-8 _*_
# created by czq on 2021/8/16


# 题目526：
# 假设有从 1 到 N 的N个整数，如果从这N个数字中成功构造出一个数组，使得数组的第 i位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一
# 个优美的排列。条件：
#
# 第i位的数字能被i整除
# i 能被第 i 位上的数字整除
# 现在给定一个整数 N，请问可以构造多少个优美的排列？


# 题解1：
# 思路：利用dfs做，维护一个visited集合，这个集合每次循环时遍历到符合数字时往集合中加入，直到循环次数到达n，则优美数列+1


def countArrangement(self, n: int) -> int:
    temp = set(i for i in range(1, n + 1))
    visited = set()
    answer = 0

    def findAnswer(i):
        nonlocal answer
        if i == n + 1:
            answer += 1
            return
        for num in temp - visited:
            if num % i == 0 or i % num == 0:
                visited.add(num)
                findAnswer(i + 1)
                visited.remove(num)

    findAnswer(1)
    return answer
