import sys

N = int(input())
nums = list()
for i in range(1, N + 1):
    nums.append(i)

pops = list(map(int, sys.stdin.readline().strip().split()))
cur_idx = 0

bucket = list()
lenl = len(nums) - 1

while len(nums) >= 2:
    e = nums[cur_idx]
    p = pops[cur_idx]
    del nums[cur_idx]
    del pops[cur_idx]
    bucket.append(e)
    if p > 0:
        cur_idx = (cur_idx + p - 1) % lenl
    else:
        cur_idx = (cur_idx + p) % lenl
    lenl -= 1

bucket.append(nums[0])
for i in range(N):
    print(bucket[i], end=' ')