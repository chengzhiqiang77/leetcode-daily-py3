# _*_ coding = utf-8 _*_
# created by czq on 2021/12/21


# 题目1154：
# 给你一个字符串date ，按 YYYY-MM-DD 格式表示一个 现行公元纪年法 日期。请你计算并返回该日期是当年的第几天。
#
# 通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。


# 题解1：
# 思路：维护一个每年各个月份中的天数，然后碰到闰年的话就在二月加1天；


def dayOfYear(self, date: str) -> int:
    year, month, day = int(date[0:4]), int(date[5:7]), int(date[8:])
    month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        month_day[1] += 1
    if month > 1:
        return sum(month_day[0:month - 1]) + day
    else:
        return day
