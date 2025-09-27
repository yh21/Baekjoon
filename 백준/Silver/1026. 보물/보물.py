import sys

N = int(input())
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))

A.sort()
B.sort(reverse=True)

sum = 0
for i in range(N):
    sum += A[i] * B[i]

print(sum)