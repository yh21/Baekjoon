import sys

N = int(input())
if N == 0:
    print(0)
    exit(0)

nums = list()
for _ in range(N):
    nums.append(int(sys.stdin.readline().strip()))

nums.sort()
disc = int(N * 15 / 100 + 0.5)

sum = 0
for i in range(disc, N - disc):
    sum += nums[i]

print(int(sum / (N - 2 * disc) + 0.5))