import sys

N = int(input())
bucket = list()
for _ in range(N):
    a, b, c = sys.stdin.readline().strip().split()
    bucket.append((a, b, c))

class node():
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

tree = {}
for root, left, right in bucket:
    tree[root] = node(root, left, right)

def preorder(node):
    print(node.root, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.root, end='')
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.root, end='')

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])