# _*_ coding = utf-8 _*_
# created by czq on 2021/8/4


# 题目611：
# 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。


# 题解1：
# 思路：a,b,c三边可以组成三角形，满足a+b>c, a+c>b, b+c>a(a,b,c大于0),可以使数组排序，两次遍历取出a,b，
# 这两个数为a,b,只需要找出满足c的个数，即为满足a，b这两边的第三条边的个数，c需要满足c<a+b,可以使用二分法找出
# b+a,这个所在的索引记为res,则abc可以组成的满足的组合有res-(j+1)
import bisect


def triangleNumber(self, nums: list[int]) -> int:
    nums.sort()
    ans = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            res = bisect.bisect_left(nums, nums[i] + nums[j]) - j - 1
            ans += max(res, 0)
    return ans


# 题解2：
# 思路：在题解1提交之后，发现运行时间过长，时间复杂度为O(n^2logn)，故而想寻找时间复杂度更低的方法，
# 在排序后，三边只需要满足nums[res] < nums[i]+nums[j]，其中i,j为题解1中类似的i,j,我们只需要找出满足的res的
# 个数，res要从i开始，防止出现i=0或i,j=0的情况


def triangleNumber(self, nums: list[int]) -> int:
    nums.sort()
    ans = 0
    for i in range(len(nums)):
        res = i
        for j in range(i + 1, len(nums)):
            while res + 1 < len(nums) and nums[res + 1] < nums[i] + nums[j]:
                res += 1
            ans += max(res - j, 0)
    return ans
