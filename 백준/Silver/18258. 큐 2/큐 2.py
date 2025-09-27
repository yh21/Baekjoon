import sys
from collections import deque

queue = deque()
bucket = list()
N = int(input())
for _ in range(N):
    oper = list(sys.stdin.readline().strip().split())
    bucket.append(oper)

for i in range(N):
    if bucket[i][0] == 'push':
        queue.append(int(bucket[i][1]))
    elif bucket[i][0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif bucket[i][0] == 'size':
        print(len(queue))
    elif bucket[i][0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif bucket[i][0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue) - 1])