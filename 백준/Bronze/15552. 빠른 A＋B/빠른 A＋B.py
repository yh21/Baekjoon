import sys

n = int(input())
test = list()
for i in range(0, n):
    num = list(map(int, sys.stdin.readline().strip().split()))
    test.append(num)

for i in range(0, n):
    print(test[i][0] + test[i][1])