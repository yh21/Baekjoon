import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())
edges = []

for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

parent = [i for i in range(V + 1)]
total_weight = 0
count = 0

for w, u, v in edges:
    if find(parent, u) != find(parent, v):
        union(parent, u, v)
        total_weight += w
        count += 1
        if count == V - 1:
            break

print(total_weight)