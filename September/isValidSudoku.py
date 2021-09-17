# _*_ coding = utf-8 _*_
# created by czq on 2021/9/17


# 题目36：
#
# 请你判断一个 9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用 '.' 表示。
#
# 注意：
#
# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。


# 题解1：
# 思路：遍历这个表格，行和列一级九宫格中没有重复出现的数字即可


def isValidSudoku(self, board: list[list[str]]) -> bool:
    def is_rows(rows_number):
        rows_answer = dict()
        for value in board[rows_number]:
            if value != ".":
                rows_answer[value] = 0
        for value in board[rows_number]:
            if value != ".":
                rows_answer[value] += 1
        for j in rows_answer.values():
            if j > 1:
                return False
        return True

    def is_columns(columns_number):
        columns_answer = dict()
        for i in range(9):
            if board[i][columns_number] != ".":
                columns_answer[board[i][columns_number]] = 0
        for i in range(9):
            if board[i][columns_number] != ".":
                columns_answer[board[i][columns_number]] += 1
        for j in columns_answer.values():
            if j > 1:
                return False
        return True

    def is_lattice(rows_number, columns_number):
        lattice_answer = dict()
        if rows_number == 0 or rows_number == 1 or rows_number == 2:
            rows_number_begin = 0
        elif rows_number == 3 or rows_number == 4 or rows_number == 5:
            rows_number_begin = 3
        else:
            rows_number_begin = 6
        if columns_number == 0 or columns_number == 1 or columns_number == 2:
            columns_number_begin = 0
        elif columns_number == 3 or columns_number == 4 or columns_number == 5:
            columns_number_begin = 3
        else:
            columns_number_begin = 6
        for i in range(rows_number_begin, rows_number_begin + 3):
            for j in range(columns_number_begin, columns_number_begin + 3):
                if board[i][j] != ".":
                    lattice_answer[board[i][j]] = 0
        for i in range(rows_number_begin, rows_number_begin + 3):
            for j in range(columns_number_begin, columns_number_begin + 3):
                if board[i][j] != ".":
                    lattice_answer[board[i][j]] += 1
        for value in lattice_answer.values():
            if value > 1:
                return False
        return True

    for i in range(9):
        if is_rows(i) and is_columns(i):
            continue
        else:
            return False
    for i in range(1, 9, 3):
        for j in range(1, 9, 3):
            if is_lattice(i, j):
                continue
            else:
                return False
    return True
