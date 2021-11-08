# _*_ coding = utf-8 _*_
# created by czq on 2021/11/8


# 题目299：
#
# 你在和朋友一起玩 猜数字（Bulls and Cows）游戏，该游戏规则如下：
#
# 写出一个秘密数字，并请朋友猜这个数字是多少。朋友每猜测一次，你就会给他一个包含下述信息的提示：
#
# 猜测数字中有多少位属于数字和确切位置都猜对了（称为 "Bulls", 公牛），
# 有多少位属于数字猜对了但是位置不对（称为 "Cows", 奶牛）。也就是说，这次猜测中有多少位非公牛数字可以通过重新排列转换成公牛数字。
# 给你一个秘密数字 secret 和朋友猜测的数字 guess ，请你返回对朋友这次猜测的提示。
#
# 提示的格式为 "xAyB" ，x 是公牛个数， y 是奶牛个数，A 表示公牛，B 表示奶牛。
#
# 请注意秘密数字和朋友猜测的数字都可能含有重复数字。


# 题解1：
# 思路：遍历两个数组，找出位置相同，且相等的元素，bulls+1，然后除去这些元素之外有相同的都为cows；
import collections


def getHint(self, secret: str, guess: str) -> str:
    bulls, cows = 0, 0
    tmp = []
    secret_tmp, guess_tmp = [], []
    str_len = len(secret)
    for i in range(str_len):
        if secret[i] == guess[i]:
            bulls += 1
        else:
            secret_tmp.append(secret[i])
            guess_tmp.append(guess[i])
    secret_ans = collections.Counter(secret_tmp)
    guess_ans = collections.Counter(guess_tmp)
    for key, value in secret_ans.items():
        cows += min(value, guess_ans[key])
    return f"{bulls}A{cows}B"
