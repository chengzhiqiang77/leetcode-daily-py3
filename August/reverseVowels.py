# _*_ coding = utf-8 _*_
# created by czq on 2021/8/19


# 题目345：
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。


# 题解1：
# 思路：维护一个双指针，分别找到左边的元音字母，右边的元音字母，找到后交换元素的位置


def reverseVowels(self, s: str) -> str:
    vowels = "aeiouAEIOU"
    s = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        while left < len(s) and s[left] not in vowels:
            left += 1
        while right > 0 and s[right] not in vowels:
            right -= 1
        if left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return "".join(s)
