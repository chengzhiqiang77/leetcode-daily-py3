# _*_ coding = utf-8 _*_
# created by czq on 2021/8/5


# 题目88：
# 给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。
#
# 初始化nums1 和 nums2 的元素数量分别为m 和 n 。你可以假设nums1 的空间大小等于m + n，这样它就有足够的空间保存来自 nums2 的元素。


# 题解1：
# 思路：将两个数组进行组合，直接用函数排序


def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1[:] = sorted(nums1[:m] + nums2[:])


def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1[:] = nums1[:m] + nums2[:]
    nums1.sort()


# 题解2：
# 思路：看到题目，nums1和nums2为两个有序数组，自然就想到了归并排序，将两个数组组合，使用归并排序进行排序


def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    def merge_op(li, low, mid, high):
        """

        :param li: 传入的数组
        :param low: 第一个有序数组的起始索引
        :param mid: 第一个有序数组的结束索引
        :param high: 数组的结尾
        :return:
        """
        i = low
        j = mid + 1
        l_tmp = []
        while i <= mid and j <= high:  # 只要左右两边都有数
            if li[i] < li[j]:
                l_tmp.append(li[i])
                i += 1
            else:
                l_tmp.append(li[j])
                j += 1
        # 循环执行完，此时有一部分没值
        while i <= mid:
            l_tmp.append(li[i])
            i += 1
        while j <= high:
            l_tmp.append(li[j])
            j += 1
        li[low:high + 1] = l_tmp

    nums1[:] = nums1[:m] + nums2[:]
    merge_op(nums1, 0, m - 1, m + n - 1)