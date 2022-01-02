# _*_ coding = utf-8 _*_
# created by czq on 2022/1/2


# 题目472：
# 给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。
#
# 连接词 定义为：一个完全由给定数组中的至少两个较短单词组成的字符串。


# 题解1：
# 思路：构造一个前缀树,用dfs来判断word是否可以由前缀树中的单词组成，如果可以，则加入到答案中，如果不行的话，则把word加入到前缀树中；


def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
    def check_word(word, pre_dict):
        if len(word) == 0:
            return True
        cur_dict = pre_dict
        for index, c in enumerate(word):
            cur_dict = cur_dict.get(c, None)
            if cur_dict is None:
                return False
            if cur_dict.get('end', 0) == 1:
                # 当前字符串前缀与树中单词匹配，递归搜索
                if check_word(word[index + 1:], pre_dict):
                    return True
        return False

    words.sort(key=lambda x: len(x))
    ans = []
    pre_dict = {}
    for item in words:
        if len(item) == 0:
            continue
        if check_word(item, pre_dict):
            ans.append(item)
        else:
            # insert word
            cur_dict = pre_dict
            for c in item:
                if cur_dict.get(c, None) is None:
                    cur_dict[c] = {}
                cur_dict = cur_dict.get(c)
            cur_dict['end'] = 1
    return ans
