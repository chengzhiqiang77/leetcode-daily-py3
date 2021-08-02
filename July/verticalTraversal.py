# _*_ coding = utf-8 _*_
# created by czq on 2021/7/31


# 题目987：
# 给你二叉树的根结点 root ，请你设计算法计算二叉树的 垂序遍历 序列。
#
# 对位于(row, col)的每个结点而言，其左右子结点分别位于(row + 1, col - 1)和(row + 1, col + 1) 。树的根结点位于 (0, 0) 。
#
# 二叉树的 垂序遍历 从最左边的列开始直到最右边的列结束，按列索引每一列上的所有结点，形成一个按出现位置从上到下排序的有序列表。如果同行同列上有多个结点，则按结点的值从小到大进行排序。
#
# 返回二叉树的 垂序遍历 序列。


# 题解1：
# 思路：按照深度优先搜索的思想，把节点所在的坐标给求出来，按照纵坐标分组，输出答案
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
    node = list()

    def dfs(root, col, cow):
        if not root:
            return
        node.append((col, cow, root.val))
        dfs(root.left, col - 1, cow + 1)
        dfs(root.right, col + 1, cow + 1)

    dfs(root, 0, 0)
    node.sort()
    line = inf
    answer = list()
    for col, cow, val in node:
        if col != line:
            line = col
            answer.append(list())
        answer[-1].append(val)
    return answer
