# _*_ coding = utf-8 _*_
# created by czq on 2021/8/23


# 题目789：
# 你在进行一个简化版的吃豆人游戏。你从 [0, 0] 点开始出发，你的目的地是target = [xtarget, ytarget] 。地图上有一些阻碍者，以数组 ghosts 给出，
# 第 i 个阻碍者从ghosts[i] = [xi, yi]出发。所有输入均为 整数坐标 。
#
# 每一回合，你和阻碍者们可以同时向东，西，南，北四个方向移动，每次可以移动到距离原位置 1 个单位 的新位置。当然，也可以选择 不动 。所有动作 同时 发生。
#
# 如果你可以在任何阻碍者抓住你 之前 到达目的地（阻碍者可以采取任意行动方式），则被视为逃脱成功。如果你和阻碍者同时到达了一个位置（包括目的地）
# 都不算是逃脱成功。
#
# 只有在你有可能成功逃脱时，输出 true ；否则，输出 false 。


# 题解1：
# 思路：该题目可以使用曼哈顿距离来求解，如果阻碍者的曼哈顿距离小于玩家的话，那么阻碍者可以到达目标等待玩家；如果阻碍者的曼哈顿距离等于玩家的话，那么
# 阻碍者可以和玩家一起到达终点；如果阻碍者的曼哈顿距离大于玩家的话，那么玩家可以逃脱成功；
from math import inf


def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
    load = abs(target[0]) + abs(target[1])
    ghosts_load = inf
    for i in ghosts:
        ghosts_load = min(ghosts_load, abs(target[0] - i[0]) + abs(target[1] - i[1]))
    return True if ghosts_load > load else False
