import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(node):
    if not tree[node]:
        return 1
    
    count = 0
    for child in tree[node]:
        count += dfs(child)
    return count

n = int(input())
parents = list(map(int, input().split()))
delete_node = int(input())

tree = [[] for _ in range(n)]
root = -1

for i in range(n):
    if parents[i] == -1:
        root = i
    else:
        tree[parents[i]].append(i)

if delete_node == root:
    print(0)
else:
    parent_of_deleted = parents[delete_node]
    tree[parent_of_deleted].remove(delete_node)

    print(dfs(root))