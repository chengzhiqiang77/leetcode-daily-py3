# _*_ coding = utf-8 _*_
# created by czq on 2021/12/4


# 题目1005：
# 给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：
#
# 选择某个下标 i并将 nums[i] 替换为 -nums[i] 。
# 重复这个过程恰好 k 次。可以多次选择同一个下标 i 。
#
# 以这种方式修改数组后，返回数组 可能的最大和 。


# 题解1：
# 思路：在可以修改的时候，先修改负数的，这样对结果的贡献是最大的，在k次没用完时，如果为偶数，可以只修改一个数字，让对结果的贡献为0，为奇数时，则
# 对结果贡献最小的数组变为负数即可


def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
    nums.sort()
    le_n = sum([i < 0 for i in nums])
    for i in range(min(le_n, k)):
        nums[i] = -1 * nums[i]
    if k - le_n > 0 and (k - le_n) % 2:
        return sum(nums) - (2 * min(nums))
    return sum(nums)
