# _*_ coding = utf-8 _*_
# created by czq on 2021/11/22


# 题目563：
#
# 给定一个二叉树，计算 整个树 的坡度 。
#
# 一个树的 节点的坡度 定义即为，该节点左子树的节点之和和右子树节点之和的 差的绝对值 。如果没有左子树的话，左子树的节点之和为 0 ；没有右子树的话也是一样。空结点的坡度是 0 。
#
# 整个树 的坡度就是其所有节点的坡度之和。


# 题解1：
# 思路：根据题目的定义，对树进行深度优先搜索即可


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findTilt(self, root: TreeNode) -> int:
    if not root:
        return 0
    self.ans = 0
    self.dfs(root)
    return self.ans


def dfs(self, node: TreeNode) -> int:
    left_sum = right_sum = 0
    if node.left:
        left_sum = self.dfs(node.left)
    if node.right:
        right_sum = self.dfs(node.right)
    self.ans += abs(left_sum - right_sum)
    return left_sum + right_sum + node.val

