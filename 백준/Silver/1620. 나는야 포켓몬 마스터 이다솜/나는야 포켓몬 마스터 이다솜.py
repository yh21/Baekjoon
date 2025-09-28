import sys

bucket = list()
N, M = map(int, sys.stdin.readline().strip().split())
for _ in range(N):
    bucket.append(sys.stdin.readline().strip())

oper = list()
for _ in range(M):
    oper.append(sys.stdin.readline().strip())

for key in oper:
    if key.isdigit() == False:
        print(bucket.index(key) + 1)
    else:
        key = int(key)
        print(bucket[key - 1])