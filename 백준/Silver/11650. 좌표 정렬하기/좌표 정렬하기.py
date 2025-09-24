import sys

n = int(input())
bucket = list()
for i in range(0, n):
    point = list(map(int, sys.stdin.readline().strip().split()))
    bucket.append(point)

bucket.sort(key = lambda x: (x[0], x[1]))
for i in range(0, n):
    print(bucket[i][0], bucket[i][1])