# _*_ coding = utf-8 _*_
# created by czq on 2021/9/28


# 题目437：
# 给定一个二叉树的根节点 root，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
#
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。


# 题解1：
# 思路：提取这个题目的意思，其实是让我们找出往下的路径中，结点数相加为targetSum的值的数量，我们可以记录每个往下的路径的值，在搜索的过程中，我们
# 可以使用深度优先搜索来遍历，我们可以用前缀和来避免重复计算；


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root: TreeNode, targetSum: int) -> int:
    def dfs(node, res):
        if not node:
            return 0
        res = [i + node.val for i in res]
        res.append(node.val)
        return res.count(targetSum) + dfs(node.right, res) + dfs(node.left, res)
    return dfs(root, [])
