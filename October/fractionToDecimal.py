# _*_ coding = utf-8 _*_
# created by czq on 2021/10/3


# 题目166：
# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。
#
# 如果小数部分为循环小数，则将循环的部分括在括号内。
#
# 如果存在多个答案，只需返回 任意一个 。
#
# 对于所有给定的输入，保证 答案字符串的长度小于 104 。


# 题解1:
# 思路：该题目中，先算出整数部分，然后依次算出小数部分，有重复的再做处理即可


def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    if numerator * denominator < 0:
        mark = "-"
    else:
        mark = ""
    integer = abs(numerator) // abs(denominator)
    remainder = abs(numerator) % abs(denominator)
    remainder_dict = {}
    decimal_part = []
    if remainder == 0:
        if integer == 0:
            return str(integer)
        else:
            return mark + str(integer)
    while remainder > 0:
        if remainder in remainder_dict:
            pos = remainder_dict[remainder]
            decimal_part.insert(pos, '(')
            decimal_part.append(')')
            break
        else:
            remainder_dict[remainder] = len(decimal_part)
            remainder *= 10
            decimal_part.append(str(remainder // abs(denominator)))
            remainder = remainder % abs(denominator)
    return mark + str(integer) + '.' + ''.join(decimal_part)
