import sys
import re

s = sys.stdin.readline().strip().strip()
result = re.findall(r'\d+|[-+]', s)

nums = list()
lenr = len(result)
for i in range(lenr):
    if result[i].isdigit():
        nums.append(result[i])

first = 0
for i in range(lenr):
    if result[i] == '-':
        first = i
        break

sum = 0
lenn = len(nums)

for i in range(lenn):
    nums[i] = int(nums[i])

if first == 0:
    for j in range(lenn):
        sum += nums[j]
else:
    for i in range(0, first // 2 + 1):
        sum += nums[i]
    for i in range(first // 2 + 1, lenn):
        sum -= nums[i]

print(sum)