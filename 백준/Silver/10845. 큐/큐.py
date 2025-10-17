import sys
from collections import deque

queue = deque()
N = int(input())
opers = list()

for _ in range(N):
    oper = list(sys.stdin.readline().strip().split())
    opers.append(oper)

for oper in opers:
    if len(oper) == 2:
        queue.append(int(oper[1]))
    elif oper[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif oper[0] == 'size':
        print(len(queue))
    elif oper[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif oper[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif oper[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue) - 1])