# _*_ coding = utf-8 _*_
# created by czq on 2021/10/28


# 题目301：
# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
#
# 返回所有可能的结果。答案可以按 任意顺序 返回。


# 题解1：
# 思路：遍历找出所有的结果，然后依次判断是否满足条件即可


def removeInvalidParentheses(self, s: str) -> list[str]:
    def isValid(s):
        cnt = 0
        for c in s:
            if c == "(":
                cnt += 1
            elif c == ")":
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0

    level = {s}
    while True:
        valid = list(filter(isValid, level))
        if valid:
            return valid
        next_level = set()
        for item in level:
            for i in range(len(item)):
                if item[i] in "()":
                    next_level.add(item[:i] + item[i + 1:])
        level = next_level
