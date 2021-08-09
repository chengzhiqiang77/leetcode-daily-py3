# _*_ coding = utf-8 _*_
# created by czq on 2021/8/10


# 题目413：
# 如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。
#
# 例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
# 给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。
#
# 子数组 是数组中的一个连续序列。


# 题解1：
# 思路：题目中所说的子数组是一个连续的数组，我们可以推导到规律，每当子数组长度加1，则他对答案的贡献n-2，
# 其中n为子数组的长度


def numberOfArithmeticSlices(self, nums: list[int]) -> int:
    n = len(nums)
    if n < 3:
        return 0
    answer = 0
    cnt = 1
    for i in range(2, n):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            answer += cnt
            cnt += 1
        else:
            cnt = 1
    return answer
