# _*_ coding = utf-8 _*_
# created by czq on 2021/8/26


# 题目881：
# 第i个人的体重为people[i]，每艘船可以承载的最大重量为limit。
#
# 每艘船最多可同时载两人，但条件是这些人的重量之和最多为limit。
#
# 返回载到每一个人所需的最小船数。(保证每个人都能被船载)。


# 题解1：
# 思路：利用贪心算法，如果最重的和最轻的人无法登上同一艘船，那么这个最重的人只能自己坐一艘船，如果可以坐同一艘小船，那么遮脸个人应该从未坐船的人里去除


def numRescueBoats(self, people: list[int], limit: int) -> int:
    people.sort()
    max_weight = len(people) - 1
    min_weight = 0
    answer = 0
    while min_weight <= max_weight:
        if people[max_weight] + people[min_weight] <= limit:
            max_weight -= 1
            min_weight += 1
        else:
            max_weight -= 1
        answer += 1
    return answer
