# 题目218：
# 城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 天际线 。
#
# 每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：
#
# lefti 是第 i 座建筑物左边缘的 x 坐标。
# righti 是第 i 座建筑物右边缘的 x 坐标。
# heighti 是第 i 座建筑物的高度。
# 天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。关键点是水平线段的左端点。列表中最后一个点是最
# 右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。
#
# 注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；三条高度为 5 的线应该在
# 最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]


# 题解1：（超时）
# 思路：把所有建筑的外观点记录下来，遍历这些点，符合条件的记录下来

import collections

def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
    building = collections.Counter()
    answer = []
    for i in buildings:
        for j in range(i[0], i[1]):
            if building[j] < i[2]:
                building[j] = i[2]
    for i in range(min(building), max(building)+1):
        if building[i] != building[i-1]:
            answer.append([i, building[i]])
    answer.append([max(building)+1, 0])
    return answer

# 题解2：
# 思路：由于所有的天际线的点都在建筑的左右边界上，所以只需要处理左右两点，利用扫描线算法，扫描到左边界是弹入该层楼高度，扫描到右边界时
# 弹出该高度，数组中存放所有可能的高度，这个数组的最大值就是当前横坐标的最大高度，扫描到高度有变化时，记录下这个点和高度，这个点就是天
# 际线的点；


def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
    pos_height = []
    for l, r, height in buildings:
        pos_height.append((l, -1 * height))
        pos_height.append((r, height))

    pos_height.sort(key=lambda x: (x[0], x[1]))

    cur_handle = [0]  # 如果是个空数组，max无法执行
    pre_max_height = 0
    cur_max_height = 0

    res = []
    for pos, height in pos_height:
        if height < 0:
            cur_handle.append(-1 * height)
        else:
            cur_handle.remove(height)
        cur_max_height = max(cur_handle)
        if pre_max_height != cur_max_height:
            res.append([pos, cur_max_height])
            pre_max_height = cur_max_height
    return res
