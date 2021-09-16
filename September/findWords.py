# _*_ coding = utf-8 _*_
# created by czq on 2021/9/16

#
# 题目212：
#
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
#
# 单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
# 同一个单元格内的字母在一个单词中不允许被重复使用。
import collections

# 题解1：
# 思路：为单词构建字典树，然后利用dfs寻找单词，但是这里要注意的是，需要使用回溯记忆，因为题意中要求不允许重复被使用


def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
    m, n = len(board), len(board[0])
    direcs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    Trie = collections.defaultdict(dict)
    for word in words:
        Trie = self.insert_word(Trie, word)
    visited = [[0] * n for _ in range(m)]
    ans = []

    def dfs(i, j, letter_node):
        letters_next = letter_node[board[i][j]]
        ending = letters_next.pop('#', False)
        if ending:
            ans.append(ending)
        for di, dj in direcs:
            i1, j1 = i + di, j + dj
            if 0 <= i1 < m and 0 <= j1 < n and visited[i1][j1] == 0 and board[i1][j1] in letter_node[board[i][j]]:
                visited[i1][j1] = 1

                dfs(i1, j1, letter_node[board[i][j]])

                visited[i1][j1] = 0

    for i in range(m):
        for j in range(n):
            if board[i][j] in Trie:
                visited[i][j] = 1
                dfs(i, j, Trie)
                visited[i][j] = 0
    return ans


def insert_word(self, Trie, word):
    cur_level = Trie
    for c in word:
        if c not in cur_level:
            cur_level[c] = collections.defaultdict(dict)
        cur_level = cur_level[c]
    cur_level['#'] = word
    return Trie
