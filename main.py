# m = {}
# s = "dddccdbba"
# for word in s:
#     m[word] = 0
# for word in s:
#     m[word] += 1
# for key,vaule in enumerate(m.values()):
#     if vaule == 1:
#         print(key)
# import collections
# s = [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]]
# dp = [[0] * (11 + 1) for _ in range(6 + 1)]
# print(dp[0][0])
# i = 20
# count = 0
# s = [1, 6, 3, 1, 2, 5]
# s = sorted(s)
# for j in range(len(s)):
#     if min(s) > i:
#         print(count)
#     else:
#         i = i - min(s)
#         count = count + 1
#         s.remove(min(s))
import bisect
import collections

# s = []
# # print(collections.Counter(s))
# m = {}
# for word in s:
#     m[word] = 0
# for word in s:
#     m[word] += 1
# print(m)
# x = sorted(m.items(), key=lambda item: item[1], reverse=True)
# for i in x:
#     print(i[0])

# strSort = []
# m = collections.Counter(s)
# x = sorted(m.items(), key=lambda item: item[1], reverse=True)
# for i in x:
#     for j in range(i[1]):
#         strSort.append(i[0])
# strSortReturn = str(strSort)
# return strSortReturn

# myName = 'cheng'
# c = collections.deque(myName, maxlen=4)
# print(c)
# c.append('z')
# c.append('h')
# c.append('i')
# print(c)

# c = collections.defaultdict(list)
# c['a'].append(1)
# c['a'].append(123)
# c['b'].append(92)
# print(c)

# c = collections.OrderedDict()
# c['a'] = 123
# c['b'] = 92
# print(c)

# s = "23123123123dfawe"
# m = collections.Counter(s)
# print(m)

# Student = collections.namedtuple('czq', ["name", "age"])
# print(Student)
# s = Student("laozhang", 20)
# print(s)

# a = {"x": 1, "y": 2}
# b = {"y": 3, "z": 4}
# c = collections.ChainMap(a, b)
# print(c['y'], c['x'], c['z'])
# del c['y']
# print(a)
# num = [1, 2, 2, 4]
# err = []
# m = collections.Counter(num)
# for word in m:
#     if m[word] == 2:
#         err.append(word)
# for i in range(len(num)):
#     if i+1 != err[0] and m[i+1] == 0:
#         err.append(i+1)
# print(err)
#
# print(num[-1])

# formula = "Mg(OH)2"
# i = 0
# stack = []
# flag = 0
# dic = {}
# n = len(formula)
# while i < n:
#     # 碰到为大写字母的情况
#     if formula[i].isupper():
#         word = ''
#         wordNumber = 0
#         word += formula[i]
#         i += 1
#         while i < n and formula[i].islower():
#             word += formula[i]
#             i += 1
#         while i < n and formula[i].isdigit():
#             wordNumber = wordNumber * 10 + int(formula[i])
#             i += 1
#         wordNumber = 1 if wordNumber == 0 else wordNumber
#         stack.append([word, wordNumber, flag])
#     # 碰到为左括号的情况
#     if i < n and formula[i] == '(':
#         flag += 1
#         i += 1
#     if i < n and formula[i] == ')':
#         multi = 0
#         i += 1
#         while i < n and formula[i].isdigit():
#             multi = 10 * multi + int(formula[i])
#             i += 1
#         multi = 1 if multi == 0 else multi
#         end = len(stack)
#         while stack and stack[end-1][2] == flag:
#             stack[end-1][1] *= multi
#             stack[end-1][2] -= 1
#             end -= 1
#         flag -= 1
# for atom in stack:
#     dic[atom[0]] = dic.get(atom[0], 0) + atom[1]
# print(dic)
# s = sorted(dic.items(), key=lambda items: items[0])
# print(s)
# ans = ''
# for atom, multi in s:
#     multi = '' if multi == 1 else multi
#     ans = atom + str(multi)
# print(ans)

# orders = [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"], ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
# foods = set()
# tables = collections.defaultdict(collections.Counter)
# print(tables)
# for name, table, food in orders:
#     foods.add(food)
#     tables[table][food] += 1
# foods = sorted(foods)
# print(tables)
# print([["Table"] + [food for food in foods]] + [[table] + [str(tables[table][food]) for food in foods] for table in sorted(tables.keys(), key=int)])
#

# n = 15
# ret = list()
# for i in range(n):
#     row = list()
#     for j in range(i+1):
#         if j == 0 or j == i:
#             row.append(1)
#         else:
#             row.append(ret[i-1][j]+ret[i-1][j-1])
#     ret.append(row)
# print(ret)

# deliciousness = [1, 1, 1, 5, 7, 9]
# ans = 0
# mod = 10**9+7
# counter = collections.Counter()
# for d in deliciousness:
#     for i in range(22):
#         if (1 << i) - d in counter:
#             ans += counter[(1 << i) - d] % mod
#     counter[d] += 1
# print(ans)
#
# print(1 << 0)
# for i in m:
#     if m[i] > 1:
#         if (m + m) % 2 == 0:
#             k += m[i]*(m[i]-1)/2
#     for j in m:
#         if i != j:
#             if (i + j) % 2 == 0:
#                 k += m[i] * m[j]
# for i in range(len(m)):
#     if m[i][1] > 1:
#         if (m[i][0] * 2) % 2 == 0:
#             k += (m[i][0]*(m[i][0]-1))/2
#     for j in range(len(m)-i-1):
#         if (m[i][0] + m[i+j+1][0])  2 == 0:
#             k += m[i][1] * m[i+j+1][1]
# print(k)

# nums = [0, 0, 0, 0, 0]
# goal = 0
# k = 0
# sum = []
# for i in range(len(nums)):
#     if i == 0:
#         sum.append(nums[i])
#     else:
#         sum.append(sum[i-1] + nums[i])
# if sum[0] == goal:
#     k = 1
# for right in range(1, len(nums)):
#     if sum[right] == goal:
#         k += 1
#     if sum[right] >= goal:
#         for left in range(right):
#             if sum[right] - sum[left] == goal:
#                 k += 1
# print(k)
# nums = [1, 2, 3, 4]
# goal = 108
# k = 0
# sum = [0 for i in range(len(nums))]
# print(sum)
# for i in range(len(nums)):
#     if i == 0:
#         sum[0] = nums[0]
#     else:
#         sum[i] = sum[i-1] + nums[i]
# if sum[0] == goal:
#     k = 1
# for right in range(1, len(nums)):
#     if sum[right] == goal:
#         k += 1
#     if sum[right] >= goal:
#         for left in range(right):
#             if sum[right] - sum[left] == goal:
#                 k += 1
#             if sum[right] - sum[left] < goal:
#                 break
# res, cur = 0, 0
# dp = collections.Counter()
# dp[0] = 1
# for i in nums:
#     cur += i
#     res += dp[cur-goal]
#     dp[cur] += 1
# print(k)
# l1 = [1,2,4]
# l2 = [1,3,4]
# l1len = len(l1)
# l2len = len(l2)
# l3len = l1len + l2len
# l3 = [0 for i in range(l3len)]
# for i in range(l1len):
#     l3[i] = l1[i]
# for i in range(l2len):
#     l3[l1len + i] = l2[i]
# print(sorted(l3))

# nums = [1,2,3]
# sum = 0
# m = collections.Counter(nums)
# for key, value in m.items():
#     print(key)
#     print(value)
# m = sorted(m.items(), key=lambda items: items[1], reverse=True)
# if len(m) == 0:
#     print(-1)
# if len(m) == 1:
#     print(m[0][1])
# for i in range(len(m)):
#     sum += m[i][1]
# if sum/m[0][1] <= 2:
#     print(m[0][0])
# if sum/m[0][1] > 2:
#     print(-1)
# tables = collections.defaultdict(collections.Counter)
# tables['for']['bar1'] = 4
# tables['for']['bar2'] = 1
# m = tables['for']
# for key,value in m.items():
#     print(value)
# citations = [1, 3, 1]
# citations = sorted(citations, reverse=True)
# print(citations)
# n = 1
# i = 1
# while citations[i-1] <= i and citations[i] <= i+1:
#     n = i
#     i += 1
# print(n)
# n = 4
# trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
# if not trust:
#     print(1)
# men, trustMen = [], []
# print(ord('b'))
# for i in trust:
#     men.append(i[0])
#     trustMen.append(i[1])
# countTrustMen = collections.Counter(trustMen)
# print(countTrustMen)
# for i in countTrustMen:
#     if countTrustMen[i] == n-1:
#         if i not in men:
#             print(i)

# letters = ["c", "f", "j"]
# letter = [ord(i) for i in letters]
# print(letter)

# buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# pos_height = []
# for l, r, height in buildings:
#     pos_height.append((l, -1 * height))
#     pos_height.append((r, height))
#     pos_height.sort(key=lambda x: (x[0],  x[1]))
#     cur_handle = []
#     for pos, height in pos_height:
#         if height < 0:
#             cur_handle.append(-1 * height)
#         else:
#             cur_handle.remove(height)
# print(pos_height)
# building = collections.Counter()
# answer = []
# for i in buildings:
#     for j in range(i[0], i[1]):
#         if building[j] < i[2]:
#             building[j] = i[2]
# for i in range(min(building), max(building)+1):
#     if building[i] != building[i-1]:
#         answer.append([i, building[i]])
# answer.append([max(building)+1, 0])
# print(answer)

# nums1 = [1, 7, 5]
# nums2 = [2, 3, 5]
# sqrt = []
# max_number = []
# sum = 0
# for i in range(len(nums1)):
#     if nums1[i] - nums2[i] < 0:
#         sqrt.append(nums2[i]-nums1[i])
#     else:
#         sqrt.append(nums1[i]-nums2[i])
# min_number = max(sqrt)
# for i in range(len(sqrt)):
#     if sqrt[i] == max(sqrt):
#         max_number.append(nums2[i])
# for i in max_number:
#     for j in nums1:
#         if 0 <= j - i < min_number:
#             min_number = j - i
#         if -min_number < j - i < 0:
#             min_number = -(j - i)
# for i in range(len(sqrt)):
#     if sqrt[i] == max(sqrt):
#         sqrt[i] = min_number
#         break
# for i in sqrt:
#     sum += i
# print(sum)
import time
from math import inf, log

# nums = [1, 5, 7]
# # idx = bisect.bisect_right(nums, 5)
# # idx1 = bisect.bisect_left(nums, 5)
# # print(idx)
# # print(idx1)
# # print(nums)
# sorted()
#
# arr = [2, 2, 1, 2, 1]
# answer = 1
# t1 = time.time()
# arr = sorted(arr)
# print(time.time()-t1)
# t2 = time.time()
# for num in arr[1:]:
#     answer = min(answer + 1, num)
# print(time.time()-t2)
# print(answer)
#
# # num = collections.Counter()
# name = ["「暑期可用」爆款回归超亲子！莫干山翠竹园·雲素+全房型可选+周末不涨！体验归居山野的纯真！",
#         "【暑期可用】安吉开臣息心庐2天1晚899送下午茶可带萌宠！拥泉而居枕山而眠，享山野静谧生活",
#         "暑期不加价！坐落浙江第 一渔村「西坡象山」毗海而居，赏日落滩涂！2晚连住送正餐，睡进乡土美学老宅里",
#         "暑期不加价！杭州不是居·林2天1晚住星眠居送正餐，野奢疗愈酒店，隐于山野森林，住独栋Villa~",
#         "【亲子爆款】必囤！三亚湾海居铂尔曼3晚连住2388起 亲子度假超高性价比之选",
#         "【亲子爆款】必囤！三亚湾海居铂尔曼2晚连住1688起 周末不加价 亲子度假超高性价比之选",
#         "「节假日通用」杭州建德航空小镇开元曼居酒店，2天1晚含餐饮消费券，5大景点门票5选1",
#         "暑期不加价！杭州不是居·林3天2晚住星眠居送千元正餐，野奢疗愈酒店，隐于山野森林，住独栋Villa~",
#         "【暑期可用】安吉开臣息心庐2天1晚899送下午茶可带萌宠！拥泉而居枕山而眠，享山野静谧生活"
#         ]
# score = [0 for i in name]
# for i in range(len(name)):
#     if "不是居" in name[i]:
#         score[i] += 100
#     if "不是" in name[i]:
#         score[i] += 40
#     if "是居" in name[i]:
#         score[i] += 40
#     if "不" in name[i]:
#         score[i] += 10
#     if "是" in name[i]:
#         score[i] += 10
#     if "居" in name[i]:
#         score[i] += 10
# print(score)
# nums = [-2,1]
# length = len(nums)
# answer = nums[0]
# sum = 0
# if length == 1:
#     print(answer)
# for i in range(length):
#     for j in range(i+1, length):
#         for z in range(i, j+1):
#             sum += nums[z]
#         answer = max(answer, sum)
#         sum = 0
# print(answer)
# for i in range(1, 1):
#     print(1)
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# answer = collections.defaultdict(list)
# for i in strs:
#     answer[''.join(sorted(i))].append(i)
# print(list(answer.values()))


# def maxFrequency(self, nums: list[int], k: int) -> int:
#     nums.sort()
#     n = len(nums)
#     l = 0
#     total = 0
#     res = 1
#     for r in range(1, n):
#         total += (nums[r] - nums[r - 1]) * (r - l)
#         while total > k:
#             total -= nums[r] - nums[l]
#             l += 1
#         res = max(res, r - l + 1)
#     return res


# arr = [-2,0,10,-19,4,6,-8]
# nums = collections.Counter(arr)
# for i in arr:
#     if i != 0 and nums[2 * i] >= 1:
#         return True
#     if i == 0 and nums[0] >= 2:
#         return True
# return False

# time = "2?:?0"
# time = list(time)
# for i in range(len(time)):
#     if i == 0 and time[i] == "?":
#         if time[1] == "?" or int(time[1]) <= 3:
#             time[i] = "2"
#         else:
#             time[i] = "1"
#     if i == 1 and time[i] == "?":
#         if time[0] == "2":
#             time[i] = "3"
#         else:
#             time[i] = "0"
#     if i == 3 and time[i] == "?":
#         time[i] = "5"
#     if i == 4 and time[i] == "?":
#         time[i] = "9"
# print("".join(time))


# adjacentPairs = [[2, 1], [3, 4], [3, 2]]
# nums = collections.defaultdict(list)
# for i, j in adjacentPairs:
#     nums[i].append(j)
#     nums[j].append(i)
# print(nums)
# for i, j in nums.items():
#     if len(j) == 1:
#         start = i
# answer = [start]
# number = start
# cur = nums[start][0]
# while True:
#     answer.append(cur)
#     if len(nums[cur]) > 1:
#         if number != nums[cur][0]:
#             number, cur = cur, nums[cur][0]
#         else:
#             number, cur = cur, nums[cur][1]
#     else:
#         break
# print(answer)
# nums = [2, 7, 11, 15]
# target = 9
# for i, j in enumerate(nums)：

enumerate()