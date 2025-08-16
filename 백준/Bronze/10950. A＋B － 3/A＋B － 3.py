import sys

n = int(input())
example = list()
for i in range(0, n):
    num = list(map(int, sys.stdin.readline().strip().split()))
    example.append(num)

for i in range(0, n):
    print(example[i][0] + example[i][1])