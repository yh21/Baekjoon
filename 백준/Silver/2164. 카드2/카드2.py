import sys
from collections import deque

queue = deque()
n = int(sys.stdin.readline().strip())
for i in range(1, n + 1):
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    card = queue[0]
    queue.append(card)
    queue.popleft()

print(queue[0])