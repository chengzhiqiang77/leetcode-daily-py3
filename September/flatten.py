# _*_ coding = utf-8 _*_
# created by czq on 2021/9/24


# 题目430：
# 多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。这些子列表也可能会有一个或多个自己的子项，
# 依此类推，生成多级数据结构，如下面的示例所示。
#
# 给你位于列表第一级的头节点，请你扁平化列表，使所有结点出现在单级双链表中。


# 题解1：
# 思路：从题目中的示例可以看出，该题目要求我们所做的扁平化过程是一个深度优先的过程，有child的先扁平化child的，然后再继续next的


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def dfs(node):
            if not node:
                return None
            if not node.child and not node.next:
                return node
            elif node.child:
                last = dfs(node.child)
                if last:
                    last.next = node.next
                if node.next:
                    node.next.prev = last
                node.next = node.child
                node.child.prev = node
                node.child = None
                return dfs(last)
            else:
                return dfs(node.next)
        dfs(head)
        return head
