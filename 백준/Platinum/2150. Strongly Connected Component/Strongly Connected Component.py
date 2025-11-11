import sys
sys.setrecursionlimit(10**5)

V, E = map(int, sys.stdin.readline().strip().split())
graph = [[] for i in range(V + 1)]
rev_graph = [[] for i in range(V + 1)]

for _ in range(E):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    rev_graph[b].append(a)

stack = list()
visited = [False] * (V + 1)

def rev_dfs(node):
    visited[node] = True

    for v in rev_graph[node]:
        if not visited[v]:
            rev_dfs(v)

    stack.append(node)

for i in range(1, V + 1):
    if not visited[i]:
        rev_dfs(i)

count = 0
visited = [False] * (V + 1)
bucket = list()

def dfs(node):
    visited[node] = True
    bucket[-1].append(node)
    for nd in graph[node]:
        if not visited[nd]:
            dfs(nd)

while stack:
    e = stack.pop()
    if not visited[e]:
        bucket.append([])
        count += 1
        dfs(e)

print(count)
for ls in bucket:
    ls.sort()
bucket.sort(key=lambda x : x[0])
for ls in bucket:
    for num in ls:
        print(num, end=' ')
    print(-1)