import sys

V = int(input())
E = int(input())

# graph
adj_mat = list()
for _ in range(V):
    adj_mat.append(list(map(int, sys.stdin.readline().strip().split())))
graph = [[] for _ in range(V + 1)]
for i in range(V):
    for j in range(V):
        if adj_mat[i][j] == 1:
            graph[i + 1].append(j + 1)

travel = list(set(list(map(int, sys.stdin.readline().strip().split()))))
lent = len(travel)
visited = [False] * (V + 1)

# dfs
def dfs(node):
    visited[node] = True
    for next in graph[node]:
        if not visited[next]:
            dfs(next)
    connected_component[-1].append(node)

connected_component = list()
for i in range(1, V + 1):
    if not visited[i]:
        connected_component.append([])
        dfs(i)

answer = False
lenc = len(connected_component)
for i in range(lenc):
    for node in travel:
        if node not in connected_component[i]:
            break
    else:
        answer = True
        break

if answer:
    print('YES')
else:
    print('NO')