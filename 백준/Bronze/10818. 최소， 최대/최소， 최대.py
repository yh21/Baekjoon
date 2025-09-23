import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
max_value = nums[0]
min_value = nums[0]

for i in range(0, n):
    if nums[i] < min_value:
        min_value = nums[i]
    if nums[i] > max_value:
        max_value = nums[i]

print(min_value, max_value)