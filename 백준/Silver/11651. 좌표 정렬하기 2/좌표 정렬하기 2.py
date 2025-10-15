import sys

N = int(input())
bucket = list()
for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    bucket.append((a, b))

bucket.sort(key=lambda x: (x[1], x[0]))
# print(bucket)
for i in range(N):
    print(bucket[i][0], bucket[i][1])