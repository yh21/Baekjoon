import sys

n = int(input())
test = list()

for _ in range(0, n):
    a, b = map(int, sys.stdin.readline().strip().split())
    test.append((a, b))

for i in range(0, n):
    print('Case #', i + 1, ': ', test[i][0] + test[i][1], sep='')