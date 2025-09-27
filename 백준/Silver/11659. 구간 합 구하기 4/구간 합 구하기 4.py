import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + nums[i - 1]

bucket = list()
for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    sum = prefix[j] - prefix[i - 1]
    bucket.append(sum)

for sums in bucket:
    print(sums)