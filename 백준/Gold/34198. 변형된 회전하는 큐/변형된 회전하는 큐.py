import sys
input = sys.stdin.read

class Node:
    __slots__ = 'prev', 'next', 'val'
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

def solve():
    data = input().split()
    if not data:
        return
    iterator = iter(data)
    
    try:
        N = int(next(iterator))
    except StopIteration:
        return

    nodes = {}
    
    first_val = int(next(iterator))
    head = Node(first_val)
    nodes[first_val] = head
    
    prev_node = head
    for _ in range(N - 1):
        val = int(next(iterator))
        new_node = Node(val)
        nodes[val] = new_node
        prev_node.next = new_node
        new_node.prev = prev_node
        prev_node = new_node
    
    tail = prev_node
    
    try:
        Q = int(next(iterator))
    except StopIteration:
        Q = 0
        
    result = []
    
    for _ in range(Q):
        cmd = next(iterator)
        
        if cmd == 'SF':
            if head != tail:
                tmp = head
                head = head.next
                head.prev = None
                tail.next = tmp
                tmp.prev = tail
                tmp.next = None
                tail = tmp
                
        elif cmd == 'SL':
            if head != tail:
                tmp = tail
                tail = tail.prev
                tail.next = None
                tmp.next = head
                head.prev = tmp
                tmp.prev = None
                head = tmp
                
        elif cmd == 'SM':
            val = int(next(iterator))
            target = nodes[val]
            
            if target == head:
                if head != tail:
                    tmp = head
                    head = head.next
                    head.prev = None
                    tail.next = tmp
                    tmp.prev = tail
                    tmp.next = None
                    tail = tmp
            elif target == tail:
                if head != tail:
                    tmp = tail
                    tail = tail.prev
                    tail.next = None
                    tmp.next = head
                    head.prev = tmp
                    tmp.prev = None
                    head = tmp
            else:
                A = target.prev
                B = target.next
                old_head = head
                old_tail = tail
                
                head = B
                head.prev = None
                tail = A
                tail.next = None
                
                old_tail.next = target
                target.prev = old_tail
                target.next = old_head
                old_head.prev = target

        elif cmd == 'PF':
            res_val = head.val
            result.append(res_val)
            
            if head == tail:
                head = None
                tail = None
            else:
                head = head.next
                head.prev = None
                
        elif cmd == 'PL':
            res_val = tail.val
            result.append(res_val)
            
            if head == tail:
                head = None
                tail = None
            else:
                tail = tail.prev
                tail.next = None
                
        elif cmd == 'PM':
            val = int(next(iterator))
            target = nodes[val]
            result.append(val)
            
            if target == head:
                if head == tail:
                    head = None
                    tail = None
                else:
                    head = head.next
                    head.prev = None
            elif target == tail:
                if head == tail:
                    head = None
                    tail = None
                else:
                    tail = tail.prev
                    tail.next = None
            else:
                prev_n = target.prev
                next_n = target.next
                prev_n.next = next_n
                next_n.prev = prev_n

    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()