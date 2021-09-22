# _*_ coding = utf-8 _*_
# created by czq on 2021/9/22


# 题目725：
# 给你一个头结点为 head 的单链表和一个整数 k ，请你设计一个算法将链表分隔为 k 个连续的部分。
#
# 每部分的长度应该尽可能的相等：任意两部分的长度差距不能超过 1 。这可能会导致有些部分为 null 。
#
# 这 k 个部分应该按照在链表中出现的顺序排列，并且排在前面的部分的长度应该大于或等于排在后面的长度。
#
# 返回一个由上述 k 部分组成的数组。


# 题解1：
# 思路：遍历整个链表，得到链表的长度，然后根据k算出分割后的列表的长度进行分割即可


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def splitListToParts(self, head: ListNode, k: int) -> list[ListNode]:
        # 获取链表长度head_length
        head_length = 0
        temp = head
        while temp:
            temp = temp.next
            head_length += 1
        # 获取分割后每个链表的长度以及额外需要添加的长度
        avg_length = head_length // k
        rem_length = head_length % k
        answer = []
        cnt = head
        for i in range(k):
            answer.append(cnt)
            temp_length = avg_length + 1 if rem_length > 0 else avg_length
            rem_length -= 1
            if cnt:
                for j in range(temp_length - 1):
                    cnt = cnt.next
                tmp = cnt.next
                cnt.next = None
                cnt = tmp
        return answer
