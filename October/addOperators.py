# _*_ coding = utf-8 _*_
# created by czq on 2021/10/18


# 题目282：
# 给定一个仅包含数字0-9的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、-或*，
# 返回所有能够得到目标值的表达式。

# 题解1：
# 思路：将所有可能的表达式列出来，再用eval方法求出这些表达式的值，符合目标值的添加到答案中


def addOperators(self, num: str, target: int) -> List[str]:
    self.ansD = {}
    ret = self.searchAll(num)
    reL = []
    for ss in ret:
        if eval(ss) == target:
            reL.append(ss)
    return reL


def searchAll(self, num):
    if num in self.ansD:
        return self.ansD[num]
    lN = len(num)
    reD = set()

    if lN == 1:
        reD.add(num)
        self.ansD[num] = reD
        return reD
    else:
        if num[0] != '0':
            reD.add(num)
    for i in range(1, lN):
        ret1 = set([num[0:i]])
        ret2 = self.searchAll(num[i:])
        for key1 in ret1:
            for key2 in ret2:
                for op in ['+', '-', '*']:
                    reD.add(key1 + op + key2)
        if num[0] == '0':
            break
    self.ansD[num] = reD
    return reD
