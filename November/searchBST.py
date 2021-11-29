# _*_ coding = utf-8 _*_
# created by czq on 2021/11/29


# 题目700：
# 给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。


# 题解1：
# 思路：二叉搜索树左子树比右子数要小，依据这个特性，进行深度优先搜索；


def searchBST(self, root, val: int):
    if not root:
        return root
    if root.val == val:
        return root
    if root.val < val:
        return self.searchBST(root.right, val)
    return self.searchBST(root.left, val)
