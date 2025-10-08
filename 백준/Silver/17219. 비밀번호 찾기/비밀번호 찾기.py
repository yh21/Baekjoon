import sys

N, M = map(int, sys.stdin.readline().strip().split())
site = list()
password = list()
for _ in range(N):
    a, b = sys.stdin.readline().strip().split()
    site.append(a)
    password.append(b)

bucket = list()
for _ in range(M):
    bucket.append(sys.stdin.readline().strip())

for st in bucket:
    print(password[site.index(st)])