import sys

N, K = map(int, sys.stdin.readline().strip().split())
bucket = list()
for _ in range(N):
    coin = int(input())
    bucket.append(coin)

bucket.sort(reverse = True)
# print(bucket) for Debugging

count = 0
for coin in bucket:
    while coin <= K:
        K -= coin
        count += 1

print(count)