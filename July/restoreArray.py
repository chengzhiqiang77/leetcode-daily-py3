# 题目1743：
# 存在一个由 n 个不同元素组成的整数数组 nums ，但你已经记不清具体内容。好在你还记得 nums 中的每一对相邻元素。
#
# 给你一个二维整数数组 adjacentPairs ，大小为 n - 1 ，其中每个 adjacentPairs[i] = [ui, vi] 表示元素 ui 和 vi 在 nums 中相邻。
#
# 题目数据保证所有由元素 nums[i] 和 nums[i+1] 组成的相邻元素对都存在于 adjacentPairs 中，存在形式可能是 [nums[i], nums[i+1]] ，也可能是
# [nums[i+1], nums[i]] 。这些相邻元素对可以 按任意顺序 出现。
#
# 返回 原始数组 nums 。如果存在多种解答，返回 其中任意一个 即可。


# 题解1：
# 思路：二维数组中，出现频率为1的数字，肯定是为原始数组的头尾数字，根据关系可以依次找出原始数组中所有的数字以及对应的关系
import collections


def t(self, adjacentPairs: list[list[int]]) -> list[int]:
    nums = collections.defaultdict(list)
    for i, j in adjacentPairs:
        nums[i].append(j)
        nums[j].append(i)
    for i, j in nums.items():
        if len(j) == 1:
            start = i
    answer = [start]
    number = start
    cur = nums[start][0]
    while True:
        answer.append(cur)
        if len(nums[cur]) > 1:
            if number != nums[cur][0]:
                number, cur = cur, nums[cur][0]
            else:
                number, cur = cur, nums[cur][1]
        else:
            break
    return answer
