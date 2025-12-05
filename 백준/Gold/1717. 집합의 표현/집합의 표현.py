import sys
sys.setrecursionlimit(10 ** 5)

N, M = map(int, sys.stdin.readline().strip().split())
root = [i for i in range(N + 1)]

def find(n):
    if root[n] != n:
        root[n] = find(root[n])
    return root[n]

def union(n, m):
    n = find(n)
    m = find(m)
    if n < m:
        root[m] = n
    else:
        root[n] = m

for _ in range(M):
    oper, a, b = map(int, sys.stdin.readline().strip().split())
    if oper == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
