import sys
sys.setrecursionlimit(10**5)

N = int(input())
answer = list()
for _ in range(N):
    V, E = map(int, sys.stdin.readline().strip().split())
    graph = [[] for i in range(V + 1)]
    rev_graph = [[] for i in range(V + 1)]
    edge = list()

    for _ in range(E):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        rev_graph[b].append(a)
        edge.append((a, b))

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
            dfs(e)

    scc_V = len(bucket)
    scc_E = [0 for _ in range(scc_V + 1)]
    scc_id = [0] * (V + 1)
    for i in range(scc_V):
        for nd in bucket[i]:
            scc_id[nd] = i + 1

    count = -1
    for eg in edge:
        if scc_id[eg[0]] != scc_id[eg[1]]:
            scc_E[scc_id[eg[1]]] += 1
    for i in range(scc_V + 1):
        if scc_E[i] == 0:
            count += 1

    answer.append(count)

for i in range(N):
    print(answer[i])