# _*_ coding = utf-8 _*_
# created by czq on 2021/11/29


# 题目423：
# 给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。


# 题解1：
# 思路：因为改字符串严格满足题目要求，所以我们可以对数字中唯一出现的先进行统计，然后对其余进行统计即可；
import collections


def originalDigits(self, s: str) -> str:
    c, cnt = collections.Counter(s), [0] * 10
    cnt[0], cnt[2], cnt[4], cnt[6], cnt[8] = c["z"], c["w"], c["u"], c["x"], c["g"]
    cnt[3], cnt[5], cnt[7] = c["h"] - cnt[8], c["f"] - cnt[4], c["s"] - cnt[6]
    cnt[1], cnt[9] = c["o"] - cnt[0] - cnt[2] - cnt[4], c["i"] - cnt[5] - cnt[6] - cnt[8]
    return "".join(str(x) * cnt[x] for x in range(10))
