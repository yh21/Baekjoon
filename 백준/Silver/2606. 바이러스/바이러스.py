import sys

V = int(sys.stdin.readline().strip())
E = int(sys.stdin.readline().strip())

graph = list()
for _ in range(V + 1):
    graph.append([])

for _ in range(E):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = list()
for _ in range(V + 1):
    visited.append(False)

def dfs(x):
    stack = [1]
    visited[x] = True
    count = 0
    while stack:
        node = stack.pop()
        for next in graph[node]:
            if visited[next] == False:
                visited[next] = True
                stack.append(next)
                count += 1
    return count

print(dfs(1))