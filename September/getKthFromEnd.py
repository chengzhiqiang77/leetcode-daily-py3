# _*_ coding = utf-8 _*_
# created by czq on 2021/9/2


# 题目剑指offer22：
# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
#
# 例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。


# 题解1：
# 思路：定义两个节点left和right，两个节点之间相差k-1，一起往后面走，当right节点走到末尾则完成，输出lefe


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
    left, right = head, head
    while right.next and k > 1:
        right = right.next
        k -= 1
    while right.next:
        left, right = left.next, right.next
    return left
