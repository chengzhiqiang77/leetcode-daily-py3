# _*_ coding = utf-8 _*_
# created by czq on 2021/10/18


# 题目230：
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。


# 题解1：
# 思路：使用深度优先搜索遍历处二叉树中所有的值存放到一个list中，将这个list排序，取出倒数第k个元素


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        root_list = []
        print(root.val)
        def dfs(root1):
            if root1:
                root_list.append(root1.val)
                dfs(root1.left)
                dfs(root1.right)
        dfs(root)
        root_list.sort()
        return root_list[k-1]
