# 题目744：
# 给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母target，请你寻找在这一有序列表里比目标字母大的最小字母。
#
# 在比较时，字母是依序循环出现的。举个例子：
#
# 如果目标字母 target = 'z' 并且字符列表为letters = ['a', 'b']，则答案返回'a'

# 题解1：
# 思路：对字符进行ascll编码，进行比较：


def nextGreatestLetter(self, letters: list[str], target: str) -> str:
    letter = [ord(i) for i in letters]
    target = ord(target)
    for i in range(len(letter)):
        if target < letter[i]:
            return letters[i]
    return letters[0]
