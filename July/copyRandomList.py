# 题目138：
# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
#
# 构造这个链表的深拷贝。深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应
# 指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。
#
# 例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。
#
# 返回复制链表的头节点。
#
# 用一个由n个节点组成的链表来表示输入/输出中的链表。每个节点用一个[val, random_index]表示：
#
# val：一个表示Node.val的整数。
# random_index：随机指针指向的节点索引（范围从0到n-1）；如果不指向任何节点，则为null。
# 你的代码 只 接受原链表的头节点 head 作为传入参数。


# 题解1：
# 思路：python的copy库中实现了深拷贝
import copy


def copyRandomList(self, head: 'Node') -> 'Node':
    return copy.deepcopy(head)


# 题解2：
# 思路：要实现深拷贝，第一步复制链表的节点索引，第二步复制链表的随机指针，第三步断开和原链表的关系


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(self, head: 'Node') -> 'Node':
    if not head:
        return head

    # 复制所有节点，插入原节点的后面
    cur = head
    while cur:
        cur.next = Node(cur.val, cur.next, None)
        cur = cur.next.next

    # 连接所有复制的节点的random指针
    cur = head
    copyHead = head.next
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next

    # 断开原链表与复制链表之间的连接
    cur = head
    cur_ = copyHead
    while cur and cur_:
        cur.next = cur_.next
        cur = cur.next
        if cur:
            cur_.next = cur.next
        cur_ = cur_.next
    return copyHead
