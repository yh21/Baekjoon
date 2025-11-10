import sys
from collections import deque

left = list(sys.stdin.readline().strip())
left = deque(left)
right = deque()
M = int(input())

method = list()
for _ in range(M):
    oper = list(sys.stdin.readline().strip())
    method.append(oper)

for oper in method:
    if oper[0] == 'L':
        if len(left) == 0:
            pass
        else:
            e = left.pop()
            right.appendleft(e)
    if oper[0] == 'D':
        if len(right) == 0:
            pass
        else:
            e = right.popleft()
            left.append(e)
    if oper[0] == 'B':
        if len(left) == 0:
            pass
        else:
            left.pop()
    if oper[0] == 'P':
        left.append(oper[2])

print("".join(left) + "".join(right))