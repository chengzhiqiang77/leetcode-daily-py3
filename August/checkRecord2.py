# _*_ coding = utf-8 _*_
# created by czq on 2021/8/18


# 题目552：
# 可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
# 'A'：Absent，缺勤
# 'L'：Late，迟到
# 'P'：Present，到场
# 如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
#
# 按 总出勤 计，学生缺勤（'A'）严格 少于两天。
# 学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。
# 给你一个整数 n ，表示出勤记录的长度（次数）。请你返回记录长度为 n 时，可能获得出勤奖励的记录情况 数量 。答案可能很大，所以返回对 109 + 7 取余
# 的结果。


# 题解1：（超时）
# 思路：利用dfs，建立一个缓存列表cache[i][j][k],i代表循环的深度-字符串长度，j代表出现a的次数，k代表连续出现L的数量，当j>=2,则该字符串不符合
# 要求，当k>=3，不符合要求，当i=0，则符合要求，答案加1；


def checkRecord(self, n: int) -> int:
    mod = 10**9 + 7
    cache = [[[-1 for i in range(3)] for _ in range(2)] for _ in range(n+1)]

    def dfs(u, anum, lnum):
        answer = 0
        if anum >= 2:
            return 0
        if lnum >= 3:
            return 0
        if u == 0:
            return 1
        if cache[u][anum][lnum] != -1:
            return cache[u][anum][lnum]
        answer = dfs(u-1, anum+1, 0) % mod
        answer = (answer + dfs(u-1, anum, lnum+1)) % mod
        answer = (answer + dfs(u-1, anum, 0)) % mod
        cache[u][anum][lnum] = answer
        return answer
    return dfs(n, 0, 0)


# 题解2：
# 思路：利用动态规划的思路来做，具体和上面思想一样


def checkRecord(self, n: int) -> int:
    mod = 10**9 + 7
    cache = [[[0 for i in range(3)] for _ in range(2)] for _ in range(n+1)]
    cache[0][0][0] = 1
    answer = 0
    for i in range(n+1):
        for j in range(2):
            for k in range(3):
                if j == 1 and k == 0:
                    cache[i][j][k] = (cache[i][j][k] + cache[i-1][j-1][0]) % mod
                    cache[i][j][k] = (cache[i][j][k] + cache[i-1][j-1][1]) % mod
                    cache[i][j][k] = (cache[i][j][k] + cache[i-1][j-1][2]) % mod
                if k != 0:
                    cache[i][j][k] = (cache[i][j][k] + cache[i-1][j][k-1]) % mod
                if k == 0:
                    cache[i][j][k] = (cache[i][j][k] + cache[i-1][j][0]) % mod
                    cache[i][j][k] = (cache[i][j][k] + cache[i-1][j][1]) % mod
                    cache[i][j][k] = (cache[i][j][k] + cache[i-1][j][2]) % mod
    for j in range(2):
        for k in range(3):
            answer += cache[n][j][k]
            answer %= mod
    return answer


# 题解3：
# 思路：偶然看到了这个思路，感觉非常有意思，有种耳目一新的感觉，在此记录一下


def checkRecord(self, n: int) -> int:
    lastll, lastl, last, alastll, alastl, alast = 0, 1, 1, 0, 0, 1
    for k in range(n):
        lastll, lastl, last, alastll, alastl, alast = lastl, last, (lastll + lastl + last) % 1000000007, alastl, f, (alastll + alastl + alast + (lastll + lastl + last) % 1000000007) % 1000000007
    return alast
