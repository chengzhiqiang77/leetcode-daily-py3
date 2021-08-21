# _*_ coding = utf-8 _*_
# created by czq on 2021/8/21


# 题目443：
# 给你一个字符数组 chars ，请使用下述算法压缩：
#
# 从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：
#
# 如果这一组长度为 1 ，则将字符追加到 s 中。
# 否则，需要向 s 追加字符，后跟这一组的长度。
# 压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。
#
# 请在 修改完输入数组后 ，返回该数组的新长度。
#
# 你必须设计并实现一个只使用常量额外空间的算法来解决此问题。


# 题解1：
# 思路：维护两个指针，一个指向字符串开始的地方，一个指向最后重复字符出现的地方


def compress(self, chars: list[str]) -> int:
    n = len(chars)
    left = 0
    answer = 0
    while left < n:
        right = left
        while right < n and chars[right] == chars[left]:
            right += 1
        chars[answer] = chars[left]
        answer += 1
        if right - left > 1:
            for c in str(right - left):
                chars[answer] = c
                answer += 1
        left = right
    return answer
