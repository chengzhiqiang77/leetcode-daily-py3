# _*_ coding = utf-8 _*_
# created by czq on 2021/8/14


# 题目1583：
# 给你一份 n 位朋友的亲近程度列表，其中 n 总是 偶数 。
#
# 对每位朋友 i，preferences[i] 包含一份 按亲近程度从高到低排列 的朋友列表。换句话说，排在列表前面的朋友与 i 的亲近程度比排在列表后面的朋友更高。每个列表中的朋友均以 0 到 n-1 之间的整数表示。
#
# 所有的朋友被分成几对，配对情况以列表 pairs 给出，其中 pairs[i] = [xi, yi] 表示 xi 与 yi 配对，且 yi 与 xi 配对。
#
# 但是，这样的配对情况可能会是其中部分朋友感到不开心。在 x 与 y 配对且 u 与 v 配对的情况下，如果同时满足下述两个条件，x 就会不开心：
#
# x 与 u 的亲近程度胜过 x 与 y，且
# u 与 x 的亲近程度胜过 u 与 v
# 返回 不开心的朋友的数目 。


# 题解1：
# 思路：首先需要看懂题目，刚开始没看懂题目走了许多弯路，首先记录每个人与队列中其他人的好感排名，如果匹配的人不是他的好感第一的话，从这个人的排名往前
# 遍历找到u，则就满足第一个条件，x与u的亲近程度胜过x与y，之后只需要判断，u所对应的v的好感排名是否超过u与x的好感排名，如果成立，则答案加1，退出循环


def unhappyFriends(self, n: int, preferences: list[list[int]], pairs: list[list[int]]) -> int:
    answer = 0
    love = [[0] * n for _ in range(n)]
    married = [0] * n
    for i in range(n):
        for j in range(n - 1):
            love[i][preferences[i][j]] = j
    for x, y in pairs:
        married[x] = y
        married[y] = x
    for x in range(n):
        y = married[x]
        love_point = love[x][y]
        for i in range(love_point):
            u = preferences[x][i]
            v = married[u]
            if love[u][x] < love[u][v]:
                answer += 1
                break
    return answer
