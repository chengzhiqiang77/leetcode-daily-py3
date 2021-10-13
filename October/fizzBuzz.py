# _*_ coding = utf-8 _*_
# created by czq on 2021/10/13


# 题目412：
# 给你一个整数 n ，找出从 1 到 n 各个整数的 Fizz Buzz 表示，并用字符串数组 answer（下标从 1 开始）返回结果，其中：
#
# answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。
# answer[i] == "Fizz" 如果 i 是 3 的倍数。
# answer[i] == "Buzz" 如果 i 是 5 的倍数。
# answer[i] == i 如果上述条件全不满足。


# 题解1：
# 思路：循环遍历从1到i，如果数字能被15整除，则为FizzBuzz，如果能被3整除，则为Fizz，能被5整除，则为Buzz，其余都为数字的字符串格式


def fizzBuzz(self, n: int) -> List[str]:
    res = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res
