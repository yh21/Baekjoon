import sys

n = int(sys.stdin.readline().strip())
bucket = list()

for _ in range(n):
    start, end = map(int, sys.stdin.readline().strip().split())
    bucket.append((start, end))

bucket.sort(key = lambda x : (x[1], x[0]))
count = 0
end_time = 0

for start, end in bucket:
    if start >= end_time:
        count += 1
        end_time = end

print(count)