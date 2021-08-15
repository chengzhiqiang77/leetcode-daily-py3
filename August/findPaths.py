# _*_ coding = utf-8 _*_
# created by czq on 2021/8/15


# 题目576：
# 给你一个大小为 m x n 的网格和一个球。球的起始坐标为 [startRow, startColumn] 。你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到
# 达网格之外）。你 最多 可以移动 maxMove 次球。
#
# 给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对 109 + 7 取余 后
# 的结果。


# 题解1：
# 思路：这题可以用动态规划来做，我们用dp[i][j][k]来表示经过i步到达（j，k）的路径数量，当i=0，j=startRow,k=startColumn,则动态规划的边界情况
# 为d[0][startRow][startColumn] = 1,当j<m or k > n,则吧该到达该点的路径数量加入答案中


def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    MOD = 10 ** 9 + 7
    outCounts = 0
    dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
    dp[0][startRow][startColumn] = 1
    for i in range(maxMove):
        for j in range(m):
            for k in range(n):
                if dp[i][j][k] > 0:
                    for j1, k1 in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
                        if 0 <= j1 < m and 0 <= k1 < n:
                            dp[i + 1][j1][k1] = (dp[i + 1][j1][k1] + dp[i][j][k]) % MOD
                        else:
                            outCounts = (outCounts + dp[i][j][k]) % MOD
    return outCounts
