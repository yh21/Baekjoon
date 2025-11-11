import sys
from collections import deque

N = int(input())
bucket = list()
for _ in range(N):
    bucket.append(list(sys.stdin.readline().strip()))

for string in bucket:
    left = deque()
    right = deque()
    for i in range(len(string)):
        if string[i] == '-':
            if left:
                left.pop()
        if string[i] == '<':
            if left:
                e = left.pop()
                right.appendleft(e)
        if string[i] == '>':
            if right:
                e = right.popleft()
                left.append(e)
        if string[i] not in ('-', '<', '>'):
            left.append(string[i])

    print("".join(left) + "".join(right))