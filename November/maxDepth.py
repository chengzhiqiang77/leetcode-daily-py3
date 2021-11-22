# _*_ coding = utf-8 _*_
# created by czq on 2021/11/22


# 题目559：
# 给定一个 N 叉树，找到其最大深度。
#
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#
# N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。


# 题解1：
# 思路：通过递归记录最大深度


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        ans = 1
        for i in root.children:
            ans = max(ans, self.maxDepth(i) + 1)
        return ans
