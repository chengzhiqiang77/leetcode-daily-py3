# _*_ coding = utf-8 _*_
# created by czq on 2021/10/12


# 题目273：
# 将非负整数 num 转换为其对应的英文表示。


# 题解1：
# 思路：题目中给定的测试用例的数字最大为十位，我们可以依次三位三位去判断（英文中单位是三位一个单位的）


def numberToWords(self, num: int) -> str:
    bit_list = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    ten_more_list = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    hundred, throusand, million, billion = "Hundred", "Thousand", "Million", "Billion"
    if num == 0:
        return "Zero"
    res = []

    def three_op(three_num):
        if three_num == 0:
            return
        hundred_bit = three_num // 100
        if hundred_bit != 0:
            res.append(bit_list[hundred_bit])
            res.append(hundred)
        three_num %= 100
        ten_bit = three_num // 10
        if ten_bit == 1:
            res.append(bit_list[three_num])
            return
        elif ten_bit == 0:
            if three_num != 0:
                res.append(bit_list[three_num])
        else:
            res.append(ten_more_list[ten_bit])
            if three_num % 10 != 0:
                res.append(bit_list[three_num % 10])

    billion_bit = num // 1000000000
    num %= 1000000000
    if billion_bit > 0:
        res.append(bit_list[billion_bit])
        res.append(billion)
    million_bit = num // 1000000
    num %= 1000000
    if million_bit > 0:
        three_op(million_bit)
        res.append(million)
    throusand_bit = num // 1000
    num %= 1000
    if throusand_bit > 0:
        three_op(throusand_bit)
        res.append(throusand)
    hundred_bit = num // 100
    num %= 100
    if hundred_bit > 0:
        res.append(bit_list[hundred_bit])
        res.append(hundred)
    three_op(num)
    if len(res) == 1:
        return res[0]
    return " ".join(res)

