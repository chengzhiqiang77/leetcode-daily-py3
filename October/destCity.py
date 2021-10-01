# _*_ coding = utf-8 _*_
# created by czq on 2021/10/1


# 题目1436：
# 给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，其中 paths[i] = [cityAi, cityBi] 表示该线路将会从 cityAi 直接前往 cityBi 。
# 请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。
#
# 题目数据保证线路图会形成一条不存在循环的线路，因此恰有一个旅行终点站。


# 题解1：
# 思路：由于题目数据保证路线图会形成一条不循环的线路，所以终点站只会在路线图的cityBi中出现；


def destCity(self, paths: list[list[str]]) -> str:
    return next(paths[i][1] for i in range(len(paths)) if paths[i][1] not in ([paths[i][0] for i in range(len(paths))]))
