# _*_ coding = utf-8 _*_
# created by czq on 2021/10/28


# 题目496：
# 给你两个 没有重复元素 的数组nums1 和nums2，其中nums1是nums2的子集。
#
# 请你找出 nums1中每个元素在nums2中的下一个比其大的值。
#
# nums1中数字x的下一个更大元素是指x在nums2中对应位置的右边的第一个比x大的元素。如果不存在，对应位置输出 -1 。


# 题解1：
# 思路：找到元素x在num2中的位置，从这个位置往后遍历找到比他大的元素；


def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
    ans = []
    n = len(nums2)
    for i in nums1:
        for j in range(nums2.index(i) + 1, n):
            if nums2[j] > i:
                ans.append(nums2[j])
                break
        else:
            ans.append(-1)
    return ans
