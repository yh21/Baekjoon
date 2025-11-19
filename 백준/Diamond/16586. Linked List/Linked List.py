import sys
import random
sys.setrecursionlimit(200000) 

def input():
    return sys.stdin.readline().strip()

N, Q = map(int, sys.stdin.readline().strip().split())

NODE_MAP = {}

class Node:
    def __init__(self, val):
        self.val = val
        self.prio = random.randint(0, 10**9)
        self.left = None
        self.right = None
        self.size = 1
        self.parent = None

def get_size(node):
    return node.size if node else 0

def update_size(node):
    if node:
        node.size = get_size(node.left) + get_size(node.right) + 1

def merge(L, R):
    if not L: return R
    if not R: return L
    
    if L.prio > R.prio:
        L.right = merge(L.right, R)
        set_child_parent(L, L.right, False)
        update_size(L)
        return L
    else:
        R.left = merge(L, R.left)
        set_child_parent(R, R.left, True)
        update_size(R)
        return R

def set_child_parent(parent, child, is_left):
    if parent:
        if is_left:
            parent.left = child
        else:
            parent.right = child
    if child:
        child.parent = parent

def split(root, k):
    if not root:
        return (None, None)
    
    left_size = get_size(root.left)
    
    if k <= left_size:
        L, R = split(root.left, k)
        root.left = R
        set_child_parent(root, R, True)
        
        if L: L.parent = None
        
        update_size(root)
        return (L, root)
    else:
        L, R = split(root.right, k - left_size - 1)
        root.right = L
        set_child_parent(root, L, False)

        if R: R.parent = None 

        update_size(root)
        return (root, R)

def get_rank_of_value(value):
    node = NODE_MAP.get(value)
    if not node:
        return -1

    rank = get_size(node.left) + 1
    current = node
    
    while current.parent:
        parent = current.parent
        if current == parent.right:
            rank += get_size(parent.left) + 1
        current = parent
    return rank

initial_array = list(range(1, N + 1))
root_treap = None

for val in initial_array:
    node = Node(val)
    NODE_MAP[val] = node
    root_treap = merge(root_treap, node)

output_distances = []

for _ in range(Q):
    try:
        line = sys.stdin.readline().strip().split()
        if not line: break
        a_val, b_val = map(int, line)
    except Exception:
        continue

    rank_a = get_rank_of_value(a_val)
    rank_b = get_rank_of_value(b_val)
    
    if rank_a == -1 or rank_b == -1:
        continue

    if rank_a < rank_b:
        new_rank_a = rank_b
    else:
        new_rank_a = rank_b + 1
    
    distance = new_rank_a - rank_a
    output_distances.append(distance)

    L1, R1 = split(root_treap, rank_a)
    L2, a_node = split(L1, rank_a - 1)
    
    merged_rest = merge(L2, R1)
    current_rank_b = rank_b
    if rank_a < rank_b:
        current_rank_b -= 1
        
    L3, R3 = split(merged_rest, current_rank_b)
    root_treap = merge(merge(L3, a_node), R3)

sys.stdout.write("\n".join(map(str, output_distances)) + "\n")

final_output_list = []
def inorder_traversal(node, result):
    if node:
        inorder_traversal(node.left, result)
        result.append(str(node.val))
        inorder_traversal(node.right, result)
        
inorder_traversal(root_treap, final_output_list)
sys.stdout.write(" ".join(final_output_list) + "\n")