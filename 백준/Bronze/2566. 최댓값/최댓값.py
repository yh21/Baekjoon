import sys

bucket = list()
for i in range(0, 9):
    nums = list(map(int, sys.stdin.readline().strip().split()))
    bucket.append(nums)

max_num = -1
cols = 0
rows = 0
for i in range(0, 9):
    for j in range(0, 9):
        if bucket[i][j] > max_num:
            max_num = bucket[i][j]
            rows = i + 1
            cols = j + 1

print(max_num)
print(rows, cols)