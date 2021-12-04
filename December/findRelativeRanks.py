# _*_ coding = utf-8 _*_
# created by czq on 2021/12/4


# 题目506：
# 给你一个长度为 n 的整数数组 score ，其中 score[i] 是第 i 位运动员在比赛中的得分。所有得分都 互不相同 。
#
# 运动员将根据得分 决定名次 ，其中名次第 1 的运动员得分最高，名次第 2 的运动员得分第 2 高，依此类推。运动员的名次决定了他们的获奖情况：
#
# 名次第 1 的运动员获金牌 "Gold Medal" 。
# 名次第 2 的运动员获银牌 "Silver Medal" 。
# 名次第 3 的运动员获铜牌 "Bronze Medal" 。
# 从名次第 4 到第 n 的运动员，只能获得他们的名次编号（即，名次第 x 的运动员获得编号 "x"）。
# 使用长度为 n 的数组 answer 返回获奖，其中 answer[i] 是第 i 位运动员的获奖情况。

# 题解1：
# 思路：对数组进行排序，记录下标，然后对分数进行处理之后，按照下标写回数组内；


def findRelativeRanks(self, score: List[int]) -> List[str]:
    ans = sorted(enumerate(score), key=lambda x: -x[1])
    n = len(ans)
    i = 0
    while i < n:
        ans[i] = list(ans[i])
        if i == 0:
            ans[i][1] = "Gold Medal"
            i += 1
        elif i == 1:
            ans[i][1] = "Silver Medal"
            i += 1
        elif i == 2:
            ans[i][1] = "Bronze Medal"
            i += 1
        else:
            ans[i][1] = str(i + 1)
            i += 1
    ans = sorted(ans, key=lambda x: x[0])
    return [i[1] for i in ans]
