# _*_ coding = utf-8 _*_
# created by czq on 2021/12/16


# 题目794：
# 给你一个字符串数组 board 表示井字游戏的棋盘。当且仅当在井字游戏过程中，棋盘有可能达到 board 所显示的状态时，才返回 true 。
#
# 井字游戏的棋盘是一个 3 x 3 数组，由字符 ' '，'X' 和 'O' 组成。字符 ' ' 代表一个空位。
#
# 以下是井字游戏的规则：
#
# 玩家轮流将字符放入空位（' '）中。
# 玩家 1 总是放字符 'X' ，而玩家 2 总是放字符 'O' 。
# 'X' 和 'O' 只允许放置在空位中，不允许对已放有字符的位置进行填充。
# 当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
# 当所有位置非空时，也算为游戏结束。
# 如果游戏结束，玩家不允许再放置字符


# 题解1：
# 思路：X先手，所以个数要么比O多一个，要么一样。两个人之间只能有一个人赢，赢的时候，X赢的话必然比O多一个，O赢的话必然和X一样多。


def validTicTacToe(self, board: list[str]) -> bool:
    x_num = 0
    o_num = 0
    mark_x = 0
    mark_0 = 0
    for i in board:
        if i[0] == i[1] == i[2]:
            if i[0] == "X":
                if mark_0:
                    return False
                mark_x = 1
            if i[0] == "O":
                if mark_x:
                    return False
                mark_0 = 1
        for j in i:
            if j == "X":
                x_num += 1
            if j == "O":
                o_num += 1
    if not (x_num - o_num == 1 or x_num == o_num):
        return False
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "X":
                if mark_0:
                    return False
                mark_x = 1
            if board[0][i] == "O":
                if mark_x:
                    return False
                mark_0 = 1
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            if mark_0:
                return False
            mark_x = 1
        if board[0][0] == "O":
            if mark_x:
                return False
            mark_0 = 1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            if mark_0:
                return False
            mark_x = 1
        if board[0][2] == "O":
            if mark_x:
                return False
            mark_0 = 1
    if mark_x and x_num - o_num == 1 or mark_0 and o_num == x_num or (not mark_0 and not mark_x):
        return True
    return False
