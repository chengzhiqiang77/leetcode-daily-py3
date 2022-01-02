# _*_ coding = utf-8 _*_
# created by czq on 2022/1/2


# 题目1609：
# 如果一棵二叉树满足下述几个条件，则可以称为 奇偶树 ：
#
# 二叉树根节点所在层下标为 0 ，根的子节点所在层下标为 1 ，根的孙节点所在层下标为 2 ，依此类推。
# 偶数下标 层上的所有节点的值都是 奇 整数，从左到右按顺序 严格递增
# 奇数下标 层上的所有节点的值都是 偶 整数，从左到右按顺序 严格递减
# 给你二叉树的根节点，如果二叉树为 奇偶树 ，则返回 true ，否则返回 false 。


# 题解1：
# 思路：利用广度优先搜索来遍历这棵树，保证这一个层上的符合单调性以及奇偶性，遍历中发现不符合返回false，遍历完返回true；


def isEvenOddTree(self, root) -> bool:
    queue = [root]
    level = 0
    while queue:
        prev = float('inf') if level % 2 else 0
        nxt = []
        for node in queue:
            val = node.val
            if val % 2 == level % 2 or level % 2 == 0 and val <= prev or level % 2 == 1 and val >= prev:
                return False
            prev = val
            if node.left:
                nxt.append(node.left)
            if node.right:
                nxt.append(node.right)
        queue = nxt
        level += 1
    return True
