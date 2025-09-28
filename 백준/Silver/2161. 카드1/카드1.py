from collections import deque

N = int(input())
queue = deque()
for i in range(1, N + 1):
    queue.append(i)

bucket = list()
while len(queue) >= 2:
    bucket.append(queue[0])
    queue.popleft()
    num = queue[0]
    queue.popleft()
    queue.append(num)

bucket.append(queue[0])
# print(bucket) for Debugging
for element in bucket:
    print(element, end=' ')