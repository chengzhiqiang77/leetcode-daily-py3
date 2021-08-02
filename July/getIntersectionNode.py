# 题目剑指 Offer 52：
# 输入两个链表，找出它们的第一个公共节点。

# 题解1：
# 思路：假设两个节点成Y相交，则L1+L2-Y（相交的部分）是相同的，则我们可以设两个点从L1和L2的头节点出发，当到链表结尾时，则换到
# 另外一个链表继续执行，则最后相交点就是公共节点


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    node1 = headA
    node2 = headB
    while node1 != node2:
        if node1:
            node1 = node1.next
        else:
            node1 = headB
        if node2:
            node2 = node2.next
        else:
            node2 = headA
    return node1
