import sys

V, E = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (V + 1)
count = 0

def dfs(v):
    visited[v] = True
    stack = list()
    stack.append(v)
    while stack:
        current = stack.pop()
        for node in graph[current]:
            if visited[node] == False:
                stack.append(node)
                visited[node] = True

for i in range(1, V + 1):
    if visited[i] == False:
        count += 1
        dfs(i)

print(count)