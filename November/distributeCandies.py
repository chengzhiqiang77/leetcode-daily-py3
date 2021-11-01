# _*_ coding = utf-8 _*_
# created by czq on 2021/11/1


# 题目575：
# 给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。
# 返回妹妹可以获得的最大糖果的种类数。
#
#
# 题解1：
# 思路：妹妹想获得最大的糖果总类数，但是需要平均分给两个人，所以此时妹妹只有两种情况，1.糖果的总类数小于糖果总数的一半，则这时候答案为糖果的最大
# 总类数；2.糖果的总类数大于糖果总数的一般，则此时答案为糖果的总数的一半；
import collections


def distributeCandies(self, candyType: list[int]) -> int:
    ans = collections.Counter(candyType)
    n = len(ans.items())
    if n <= len(candyType) // 2:
        return n
    else:
        return len(candyType) // 2
