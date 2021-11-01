# _*_ coding = utf-8 _*_
# created by czq on 2021/11/1


# 题目355：
# 给你一个整数数组 distance 。
#
# 从 X-Y 平面上的点(0,0)开始，先向北移动 distance[0] 米，然后向西移动 distance[1] 米，向南移动 distance[2] 米，
# 向东移动 distance[3] 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。
#
# 判断你所经过的路径是否相交。如果相交，返回 true ；否则，返回 false 。


# 题解1：
# 思路：归纳统计路径相交的几种情况，我们只需要计算前六次的路径相交情况即可，因为六次后可以视为一个循环；
# 归纳得出：
# 第一类：
# 这种路径交叉需满足以下条件：
# 第 i-1 次移动距离小于等于第 i-3 次移动距离。
# 第 i 次移动距离大于等于第 i-2 次移动距离。
#
# 第二类：
# 这种路径交叉需要满足以下条件：
#
# 第 4 次移动距离等于第 2 次移动距离。
# 第 5 次移动距离大于等于第 3 次移动距离减第 1 次移动距离的差；注意此时第 3 次移动距离一定大于第 1 次移动距离，否则在上一步就已经出现第 1 类路径交叉的情况了。
#
# 第三类：
#
# 这种路径交叉需满足以下条件：
#
# 第 i-1 次移动距离大于等于第 i-3 次移动距离减第 i-5 次移动距离的差，且小于等于第 i-3 次移动距离；注意此时第 i-3 次移动距离一定大于第 i-5 次移动距离，否则在两步之前就已经出现第 1 类路径交叉的情况了。
# 第 i-2 次移动距离大于第 i-4 次移动距离；注意此时第 i-2 次移动距离一定不等于第 i-4 次移动距离，否则在上一步就会出现第 3 类路径交叉（或第 2 类路径交叉）的情况了。
# 第 ii 次移动距离大于等于第 i-2 次移动距离减第 i-4 次移动距离的差。


def isSelfCrossing(self, distance: list[int]) -> bool:
    n = len(distance)
    for i in range(3, n):
        # 第 1 类路径交叉的情况
        if (distance[i] >= distance[i - 2]
                and distance[i - 1] <= distance[i - 3]):
            return True

        # 第 2 类路径交叉的情况
        if i == 4 and (distance[3] == distance[1]
                       and distance[4] >= distance[2] - distance[0]):
            return True

        # 第 3 类路径交叉的情况
        if i >= 5 and (distance[i - 3] - distance[i - 5] <= distance[i - 1] <= distance[i - 3]
                       and distance[i] >= distance[i - 2] - distance[i - 4]
                       and distance[i - 2] > distance[i - 4]):
            return True
    return False
