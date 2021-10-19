# _*_ coding = utf-8 _*_
# created by czq on 2021/10/19


# 题目211：
# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
#
# 实现词典类 WordDictionary ：
#
# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与word 匹配，则返回 true ；否则，返回 false 。word 中可能包含一些 '.' ，每个. 都可以表示任何一个字母。


# 题解1：
# 思路：定义一个字典，将加入到该字典按照单词长度分类，查找时，只需根据目标字符串的长度，在字典中查找，是否存在即可，在这里，查找可以使用正则来查
import re


class WordDictionary:

    def __init__(self):
        self.word_dict = {}

    def addWord(self, word: str) -> None:
        word_length = len(word)
        if word_length not in self.word_dict:
            self.word_dict[word_length] = [word]
        else:
            self.word_dict[word_length].append(word)

    def search(self, word: str) -> bool:
        if len(word) not in self.word_dict:
            return False
        for i in self.word_dict[len(word)]:
            flag = re.search(word, i, flags=0)
            if flag is not None:
                return True
        return False
