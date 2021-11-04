# _*_ coding = utf-8 _*_
# created by czq on 2021/11/4


# 题目237：
# 请编写一个函数，用于 删除单链表中某个特定节点 。在设计函数时需要注意，你无法访问链表的头节点head ，只能直接访问 要被删除的节点 。
#
# 题目数据保证需要删除的节点 不是末尾节点 。


# 题解1：
# 思路：由于数据保证了删除的节点不是末尾节点，所以我们可以把要当前删除的节点值置为下一个节点的值，然后把下一个节点删除即可；


def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next
