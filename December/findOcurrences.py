# _*_ coding = utf-8 _*_
# created by czq on 2022/1/2


# 题目1078：
# 给出第一个词first 和第二个词second，考虑在某些文本text中可能以 "first second third" 形式出现的情况，其中second紧随first出现，third紧随second出现。
#
# 对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。


# 题解1：
# 思路：将字符串以单词纬度分割成一个list，遍历这个list模拟即可；


def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
    a = text.split(" ")
    n = len(a)
    target = 0
    res = []
    while target < n:
        if a[target] == first:
            if target + 1 < n and a[target + 1] == second:
                if target + 2 < n:
                    res.append(a[target + 2])
                    target += 1
                else:
                    target += 1
            else:
                target += 1
        else:
            target += 1
    return res
