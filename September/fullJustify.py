# _*_ coding = utf-8 _*_
# created by czq on 2021/9/9


# 题目68：
# 给定一个单词数组和一个长度maxWidth，重新排版单词，使其成为每行恰好有maxWidth个字符，且左右两端对齐的文本。
#
# 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格' '填充，使得每行恰好有 maxWidth个字符。
#
# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
#
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
#
# 说明:
#
# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于maxWidth。
# 输入单词数组 words至少包含一个单词。


# 题解1：
# 思路：对题目进行模拟即可，我们来提取题目的条件：每行的长度不能超过给定的maxWidth，我们在考虑长度时，必须给两个字母间留下一个空格的位置，
# 空格的长度至少为这行所放词数-1；而对于填充空格，如果是最后一行的话，则在单词之间填充一个空格即可，其他空格都在右边填充直到达到最长长度，
# 如果改行只有一个单词的话，则在右边填充字符；对于其他的情况，在每行之间填充的空格数为空格总数整除所放词数-1，需要额外增加一个空格的为前
# （空格总数取模所放词数-1）的单词；


def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
    right, n = 0, len(words)
    ans = []
    answer = ""
    blank = ""
    while True:
        if right == n:
            break
        left = right
        words_len = 0
        blank = ""
        while right < n and maxWidth >= words_len + len(words[right]) + right - left:
            words_len += len(words[right])
            right += 1
        if right == n:
            answer = " ".join(words[left:right])
            for i in range(maxWidth - len(answer)):
                blank += " "
            answer += blank
            ans.append(answer)
        elif right - left == 1:
            answer = words[left]
            for i in range(maxWidth - len(answer)):
                blank += " "
            answer += blank
            ans.append(answer)
        else:
            avgBlank = (maxWidth - words_len) // (right - left - 1)
            addBlank = (maxWidth - words_len) % (right - left - 1)
            if not addBlank:
                for i in range(avgBlank):
                    blank += " "
                avg_blank_str = blank.join(words[left:right])
                ans.append(avg_blank_str)
            else:
                blank = ""
                for i in range(avgBlank + 1):
                    blank += " "
                add_str = blank.join(words[left:left + addBlank + 1])
                blank = ""
                for i in range(avgBlank):
                    blank += " "
                avg_blank_str = blank.join(words[left + addBlank + 1:right])
                blank = ""
                for i in range(avgBlank):
                    blank += " "
                ans.append(add_str + blank + avg_blank_str)
    return ans