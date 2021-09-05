# _*_ coding = utf-8 _*_
# created by czq on 2021/9/5


# 题目470：
# 已有方法rand7可生成 1 到 7 范围内的均匀随机整数，试写一个方法rand10生成 1 到 10 范围内的均匀随机整数。
#
# 不要使用系统的Math.random()方法。


# 题解1：
# 思路：要均匀生成1～10的随机整数，所以rand7肯定是不够的，我们取一次rand7，只取其1～5，这样取到1～5的概率都是1/5，只需要在执行一次rand7，使得取到
# 数的概率为1/2，且两个数相加在1～10内
import random


def rand7():
    return random.randint(1, 7)


def rand10(self):
    number1 = rand7()
    while number1 > 5:
        number1 = rand7()
    number2 = rand7()
    while number2 > 6:
        number2 = rand7()
    return (number1 << 1) - (number2 & 1)
