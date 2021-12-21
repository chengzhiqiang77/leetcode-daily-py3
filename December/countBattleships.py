# _*_ coding = utf-8 _*_
# created by czq on 2021/12/21


# 题目419：
# 给你一个大小为 m x n 的矩阵 board 表示甲板，其中，每个单元格可以是一艘战舰 'X' 或者是一个空位 '.' ，返回在甲板 board 上放置的 战舰 的数量。
#
# 战舰 只能水平或者垂直放置在 board 上。换句话说，战舰只能按 1 x k（1 行，k 列）或 k x 1（k 行，1 列）的形状建造，其中 k 可以是任意大小。两艘战舰之间至少有一个水平或垂直的空位分隔 （即没有相邻的战舰）。


# 题解1：
# 思路：遍历整个甲板，如果甲板上有战舰，而且这个战舰之前没被记录过，则战舰数量加1；


def countBattleships(self, board: list[list[str]]) -> int:
    Row = len(board)
    Col = len(board[0])
    res = 0
    for r in range(Row):
        for c in range(Col):
            if board[r][c] == 'X':
                if 0 <= r - 1 and board[r - 1][c] == 'X':
                    continue
                if 0 <= c - 1 and board[r][c - 1] == 'X':
                    continue
                res += 1
    return res
