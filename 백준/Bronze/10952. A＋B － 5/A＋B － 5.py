import sys

sum = list()
n = 0
while True:
    a, b = map(int, sys.stdin.readline().strip().split())
    if (a + b) != 0:
        sum.append(a + b)
        n += 1
    else:
        break

for i in range(0, n):
    print(sum[i])