# _*_ coding = utf-8 _*_
# created by czq on 2021/12/10


# 题目1034：
# 给你一个大小为 m x n 的整数矩阵 grid ，表示一个网格。另给你三个整数row、col 和 color 。网格中的每个值表示该位置处的网格块的颜色。
#
# 两个网格块属于同一 连通分量 需满足下述全部条件：
#
# 两个网格块颜色相同
# 在上、下、左、右任意一个方向上相邻
# 连通分量的边界 是指连通分量中满足下述条件之一的所有网格块：
#
# 在上、下、左、右任意一个方向上与不属于同一连通分量的网格块相邻
# 在网格的边界上（第一行/列或最后一行/列）
# 请你使用指定颜色color 为所有包含网格块grid[row][col] 的 连通分量的边界 进行着色，并返回最终的网格grid 。


# 题解1：
# 思路：利用bfs将连通分量找出来，然后把四面都存在的点去掉，修改颜色即可；


def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
    ans = []
    target = grid[row][col]
    row_n = len(grid)
    col_n = len(grid[0])

    def bfs(a, b):
        if grid[a][b] == target:
            if [a, b] not in ans:
                ans.append([a, b])
            else:
                return
        else:
            return
        if a + 1 < row_n and [a + 1, b] not in ans:
            bfs(a + 1, b)
        if a - 1 > -1 and [a - 1, b] not in ans:
            bfs(a - 1, b)
        if b + 1 < col_n and [a, b + 1] not in ans:
            bfs(a, b + 1)
        if b - 1 > -1 and [a, b - 1] not in ans:
            bfs(a, b - 1)
        return

    bfs(row, col)
    for i in ans:
        if not ([i[0] + 1, i[1]] in ans and [i[0] - 1, i[1]] in ans and [i[0], i[1] + 1] in ans and [i[0],
                                                                                                     i[1] - 1] in ans):
            grid[i[0]][i[1]] = color
    return grid
