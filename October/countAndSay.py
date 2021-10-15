# _*_ coding = utf-8 _*_
# created by czq on 2021/10/15


# 题目38：
# 给定一个正整数 n ，输出外观数列的第 n 项。
#
# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
#
# 你可以将其视作是由递归公式定义的数字字符串序列：
#
# countAndSay(1) = "1"
# countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。


# 题解1：
# 思路：我们设计一个识别的算法，对n-1的字符串进行遍历，当后一个字符串和当前字符串一样，则计数+1，当不一样时，则将数量+字符串加上，然后计数=1，字符串
# 为不一样的字符串，继续遍历，重复这个过程


def countAndSay(self, n: int) -> str:
    count_and_say = ans = "1"
    for i in range(2, n + 1):
        count_and_say, ans, count = ans, "", 0
        str_ans = count_and_say[0]
        for j in range(0, len(count_and_say)):
            if count_and_say[j] == str_ans:
                count += 1
            else:
                ans += str(count) + str(count_and_say[j - 1])
                count,
                str_ans = 1, count_and_say[j]
        if count != 0:
            ans += str(count) + str(count_and_say[-1])
    return ans
