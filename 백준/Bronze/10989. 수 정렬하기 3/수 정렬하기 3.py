import sys

n = int(sys.stdin.readline().strip())
arr = [0] * 10001
for _ in range(0, n):
    number = int(sys.stdin.readline().strip())
    arr[number] += 1

for i in range(1, 10001):
    if arr[i] >= 1:
        for j in range(0, arr[i]):
            print(i)