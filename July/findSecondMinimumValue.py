# _*_ coding = utf-8 _*_
# created by czq on 2021/7/27


# 题目671：
# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为2或0。如果一个节点有两个子节点的话，那么该节点的值等于
# 两个子节点中较小的一个。
#
# 更正式地说，root.val = min(root.left.val, root.right.val) 总成立。
#
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。


# 题解1：
# 思路：通过dfs把树所有的值去重然后遍历出来并排序，如果只有一个值，返回-1，否则则返回第二小的值


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findSecondMinimumValue(self, root: TreeNode) -> int:
    self.s = set()
    self.dfs(root)
    self.answer = list(self.s)
    self.answer.sort()
    if len(self.answer) == 1:
        return -1
    else:
        return self.answer[1]


def dfs(self, root: TreeNode) -> list:
    if not root:
        return
    self.s.add(root.val)
    self.dfs(root.right)
    self.dfs(root.left)
