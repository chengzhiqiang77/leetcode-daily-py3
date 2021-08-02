# 题目726：
# 给定一个化学式formula（作为字符串），返回每种原子的数量。
#
# 原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。
#
# 如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。
#
# 两个化学式连在一起是新的化学式。例如H2O2He3Mg4 也是化学式。
#
# 一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。
#
# 给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。

# 示例 1:
#
# 输入:
# formula = "H2O"
# 输出: "H2O"
# 解释:
# 原子的数量是 {'H': 2, 'O': 1}。

# 示例 2:
#
# 输入:
# formula = "Mg(OH)2"
# 输出: "H2MgO2"
# 解释:
# 原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。

# 示例 3:
#
# 输入:
# formula = "K4(ON(SO3)2)2"
# 输出: "K4N2O14S4"
# 解释:
# 原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。

# 题解1：
# 思路：由题意可得，给定的字符串中，只有五种元素：大写字母，小写字母，数字，左括号，右括号；分析可得：
# 可分为三种情况：1.大写字母；2.左括号；3.右括号；对这三种情况进行分析
# 大写字母：遍历到大写字母后继续遍历，如果是一个大写字母的话停止，且把出现频率置为1；如果是一个小写字母，则加入到该原子的名称中；如果遍历到的是数字，则把原频率向右
# 移一位（乘10）再加上遍历到的数字；
# 左括号：遍历到左括号的话，将之后遍历到的所有原子的出现倍数加1
# 右括号：遍历到右括号的话，继续遍历，如果未遍历到数字的话，则将倍数置为1，然后将出现倍数等于当前出现倍数的，出现频率=出现倍数*倍数；遍历到数字，则把原倍数向右
# 移动一位（乘10）再加上遍历到的数字，遍历完之后，出现频率=出现倍数*倍数；
# 所有处理完之后，得到一个数组，将数组进行处理，得到字典，将字典按序排序，进行处理，得到字符串


def countOfAtoms(self, formula: str) -> str:
    i = 0
    stack = []
    flag = 0
    dic = {}
    n = len(formula)
    while i < n:
        # 碰到为大写字母的情况
        if formula[i].isupper():
            word = ''
            word_number = 0
            word += formula[i]
            i += 1
            while i < n and formula[i].islower():
                word += formula[i]
                i += 1
            while i < n and formula[i].isdigit():
                word_number = word_number * 10 + int(formula[i])
                i += 1
            if word_number == 0:
                word_number = 1
            stack.append([word, word_number, flag])
        # 碰到为左括号的情况
        if i < n and formula[i] == '(':
            flag += 1
            i += 1
        # 碰到为右括号的情况
        if i < n and formula[i] == ')':
            multi = 0
            i += 1
            while i < n and formula[i].isdigit():
                multi = multi * 10 + int(formula[i])
                i += 1
            multi = 1 if multi == 0 else multi
            end = len(stack)
            while stack and stack[end - 1][2] == flag:
                stack[end - 1][1] *= multi
                stack[end - 1][2] -= 1
                end -= 1
            flag -= 1
    # 处理得到字典
    for atom in stack:
        dic[atom[0]] = dic.get(atom[0], 0) + atom[1]
    # 对字典处理得到字符串
    s = sorted(dic.items(), key=lambda items: items[0])
    ans = ''
    for atom, multi in s:
        multi = '' if multi == 1 else multi
        ans += atom + str(multi)
    return ans
