import sys
from collections import deque

# graph
N, M = map(int, sys.stdin.readline().strip().split())
graph = list()
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))

queue = deque([(0, 0)])

horiz = [0, 0, 1, -1]
vert = [1, -1, 0, 0]

while len(queue) != 0:
    x, y = queue.popleft()
    for i in range(4):
        next_x, next_y = x + horiz[i], y + vert[i]
        if N > next_x >= 0 and M > next_y >= 0:
            if graph[next_x][next_y] == 1:
                queue.append((next_x, next_y))
                graph[next_x][next_y] = graph[x][y] + 1

print(graph[N - 1][M - 1])