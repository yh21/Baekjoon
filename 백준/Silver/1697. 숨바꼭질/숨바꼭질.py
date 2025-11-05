import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
visited = [-1] * 100001

def BFS():
    queue = deque([N])
    visited[N] = 0

    while queue:
        current = queue.popleft()

        if current == K:
            return visited[K]
    
        for next in (current + 1, current * 2, current - 1):
            if 0 <= next <= 100000 and visited[next] == -1:
                queue.append(next)
                visited[next] = visited[current] + 1

print(BFS())