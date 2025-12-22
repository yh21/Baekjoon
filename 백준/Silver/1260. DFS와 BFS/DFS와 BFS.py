import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)

# grpah
V, E, first = map(int, sys.stdin.readline().strip().split())
dfsgraph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, sys.stdin.readline().strip().split())
    dfsgraph[a].append(b)
    dfsgraph[b].append(a)

for i in range(V + 1):
    dfsgraph[i].sort()

bfsgraph = dfsgraph
stack = list()
queue = deque()
visited = [False] * (V + 1)

# dfs
def dfs(v):
    visited[v] = True
    print(v, end=' ')    
    for node in dfsgraph[v]:
        if not visited[node]:
            dfs(node)

# bfs
visited2 = [False] * (V + 1)
def bfs(v):
    visited2[v] = True
    queue.append(v)
    while queue:
        e = queue.popleft()
        print(e, end=' ')
        for node in bfsgraph[e]:
            if not visited2[node]:
                queue.append(node)
                visited2[node] = True

dfs(first)
print()
bfs(first)