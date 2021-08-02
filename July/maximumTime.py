# 题目1736：
# 给你一个字符串 time ，格式为 hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。
#
# 有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。
#
# 替换time 中隐藏的数字，返回你可以得到的最晚有效时间。


# 题解1：
# 思路：该题目用贪心算法，从第高位往低位遍历，保证高位取最大即可


def maximumTime(self, time: str) -> str:
    time = list(time)
    for i in range(len(time)):
        if i == 0 and time[i] == "?":
            if time[1] == "?" or int(time[1]) <= 3:
                time[i] = "2"
            else:
                time[i] = "1"
        if i == 1 and time[i] == "?":
            if time[0] == "2":
                time[i] = "3"
            else:
                time[i] = "9"
        if i == 3 and time[i] == "?":
            time[i] = "5"
        if i == 4 and time[i] == "?":
            time[i] = "9"
    return "".join(time)