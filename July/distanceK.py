# _*_ coding = utf-8 _*_
# created by czq on 2021/7/28


# 题目863：
# 给定一个二叉树（具有根结点root），一个目标结点target，和一个整数值 K 。
#
# 返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
#
# 提示：
#
# 给定的树是非空的。
# 树上的每个结点都具有唯一的值0 <= node.val <= 500。
# 目标结点target是树上的结点。
# 0 <= K <= 1000.


# 题解1：
# 思路：使用bfs的思想，因为树上每一个节点都具有唯一的值，所以值不会重复，只需要遍历从target开始的第k层，获取所有节点
# 的值，再加上网上遍历的值，就是本题的答案


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
    def findParents(tree):
        if not tree:
            return
        if tree.left:
            tree.left.par = tree
            findParents(tree.left)
        if tree.right:
            tree.right.par = tree
            findParents(tree.right)

    findParents(root)
    root.par = None
    nodes = [target]
    seen = {target}
    for _ in range(k):
        temp = []
        for node in nodes:  # 处理当前层每个节点，找寻其下一层且未发现的节点
            for n in (node.left, node.right, node.par):
                if n and n not in seen:
                    seen.add(n)
                    temp.append(n)
        nodes = temp
    return [n.val for n in nodes]
