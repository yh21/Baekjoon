import sys

N = int(input())
nums = list()
for _ in range(N):
    nums.append(int(sys.stdin.readline().strip()))

ls0 = [-1] * 41
ls1 = [-1] * 41
ls0[0] = 1
ls0[1] = 0
ls1[0] = 0
ls1[1] = 1

for i in range(2, 41):
    ls0[i] = ls0[i - 1] + ls0[i - 2]
    ls1[i] = ls1[i - 1] + ls1[i - 2]

for num in nums:
    print(ls0[num], ls1[num])