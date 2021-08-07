# _*_ coding = utf-8 _*_
# created by czq on 2021/8/7


# 题目457：
# 存在一个不含 0 的 环形 数组nums ，每个 nums[i] 都表示位于下标 i 的角色应该向前或向后移动的下标个数：
#
# 如果 nums[i] 是正数，向前 移动 nums[i] 步
# 如果nums[i] 是负数，向后 移动 nums[i] 步
# 因为数组是 环形 的，所以可以假设从最后一个元素向前移动一步会到达第一个元素，而第一个元素向后移动一步会到达最后一个元素。
#
# 数组中的 循环 由长度为 k 的下标序列 seq ：
#
# 遵循上述移动规则将导致重复下标序列 seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
# 所有 nums[seq[j]] 应当不是 全正 就是 全负
# k > 1
# 如果 nums 中存在循环，返回 true ；否则，返回 false 。


# 题解1：
# 思路：依次遍历环中的点，把点的坐标和下一个点坐标存入到字典中，如果我们走到下一个点时，他的下一个点坐标在
# 字典中的话，我们则认为这个数组中存在循环，我们使用mark来标记数组中的点是否走过


def circularArrayLoop(self, nums: list[int]) -> bool:
    def nextPos(pos):
        return ((pos + nums[pos]) % n + n) % n

    n = len(nums)
    mark = [None for _ in range(n)]  # 记录该点是否已经被走过
    for i in range(n):
        if mark[i]:
            continue
        mark[i] = 1
        mp = dict()  # 创建字典，key为该元素所在位置的索引，value为该下一步元素所在的索引
        pos = i
        while True:
            next_pos = nextPos(pos)
            if next_pos == pos or nums[next_pos] * nums[pos] < 0:
                break
            if next_pos in mp:
                return True
            mp[pos] = next_pos
            pos = next_pos
            mark[pos] = 1
    return False
