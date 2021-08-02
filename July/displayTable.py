# 题目1418：
# 给你一个数组 orders，表示客户在餐厅中完成的订单，确切地说， orders[i]=[customerNamei,tableNumberi,foodItemi] ，其中 customerNamei
# 是客户的姓名，tableNumberi 是客户所在餐桌的桌号，而 foodItemi 是客户点的餐品名称。
#
# 请你返回该餐厅的 点菜展示表 。在这张表中，表中第一行为标题，其第一列为餐桌桌号 “Table” ，后面每一列都是按字母顺序排列的餐品名称。接下来每一行中
# 的项则表示每张餐桌订购的相应餐品数量，第一列应当填对应的桌号，后面依次填写下单的餐品数量。
#
# 注意：客户姓名不是点菜展示表的一部分。此外，表中的数据行应该按餐桌桌号升序排列。

# 题解1：
# 思路：由题意可得出，该表由几个数组组成，第一个数组为菜品的名称，后续数组为各个桌点该菜品的数量，由此，我们需要一个列表和一个复合字典，复合字典用于
# 存储桌号的对应菜品点的数量
import collections


def displayTable(self, orders: list[list[str]]) -> list[list[str]]:
    foods = set()
    tables = collections.defaultdict(collections.Counter)
    for name, table, food in orders:
        foods.add(food)
        tables[table][food] += 1
    foods = sorted(foods)
    return [["Table"] + [food for food in foods]] + [[table] + [str(tables[table][food]) for food in foods] for table in
                                                     sorted(tables.keys(), key=int)]