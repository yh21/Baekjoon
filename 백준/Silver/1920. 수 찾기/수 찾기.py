import sys

N = int(input())
nums = set(map(int, sys.stdin.readline().strip().split()))
M = int(input())
keys = list(map(int, sys.stdin.readline().strip().split()))

for key in keys:
    print(1 if key in nums else 0)