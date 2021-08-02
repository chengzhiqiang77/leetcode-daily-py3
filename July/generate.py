# 题目118：
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

# 题解1：
# 杨辉三角一个重要的特性就是每个数的左上方和右上方的和为这个数，我们把杨辉三角左对齐，可以得到一个结论，每个数的值为：这个数上方的数与这个数左上方数和

def generate(self, numRows: int) -> list[list[int]]:
    ret = list()
    for i in range(numRows):
        row = list()
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(ret[i - 1][j] + ret[i - 1][j - 1])
        ret.append(row)
    return ret

