import sys

total_cost = int(input())
n = int(input())
test = list()

for _ in range(0, n):
    cost, amount = map(int, sys.stdin.readline().strip().split())
    test.append((cost, amount))

for i in range(0, n):
    total_cost -= test[i][0] * test[i][1]

if total_cost == 0:
    print('Yes')
else:
    print('No')