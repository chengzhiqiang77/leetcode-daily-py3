# _*_ coding = utf-8 _*_
# created by czq on 2021/7/29


# 题目1104：
# 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按“之” 字形进行标记。
#
# 如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；
#
# 而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。
#
# 给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。


# 题解1：
# 思路：首先阅读题目可得这是一个在2^n行镜像翻转的完全二叉树，所以可以将在完全二叉树的情况求出来，再对部分答案进行
# 镜像翻转


def pathInZigZagTree(self, label: int) -> list[int]:
    answer = []
    while label > 0:
        answer.append(label)
        label = label // 2
    answer.reverse()
    for i in range(len(answer) - 2, -1, -2):
        original = answer[i]
        start = 2 ** i
        end = 2 ** (i + 1) - 1
        new = end - original + start
        answer[i] = new
    return answer
ord()
