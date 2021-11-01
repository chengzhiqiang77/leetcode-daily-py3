# _*_ coding = utf-8 _*_
# created by czq on 2021/11/1


# 题目500：
# 给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。
#
# 美式键盘 中：
#
# 第一行由字符 "qwertyuiop" 组成。
# 第二行由字符 "asdfghjkl" 组成。
# 第三行由字符 "zxcvbnm" 组成。


# 题解1：
# 思路：对字符串的字符依次判断，所有在一行内则加入答案中


def findWords(self, words: list[str]) -> list[str]:
    ans = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    res = []
    for word in words:
        is_mark = True
        if word[0].lower() in ans[0]:
            target = 1
        elif word[0].lower() in ans[1]:
            target = 2
        else:
            target = 3
        for i in range(1, len(word)):
            if word[i].lower() not in ans[target - 1]:
                is_mark = False
                break
        if is_mark:
            res.append(word)
    return res
