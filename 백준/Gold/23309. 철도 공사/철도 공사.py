import sys

input_data = sys.stdin.read().split()

def solve():
    iterator = iter(input_data)
    
    N = int(next(iterator))
    M = int(next(iterator))
    nxt = [0] * 1000001
    prv = [0] * 1000001
    
    stations = []
    for _ in range(N):
        stations.append(int(next(iterator)))
        
    for i in range(N):
        curr = stations[i]
        left = stations[i - 1]
        right = stations[(i + 1) % N]
        
        prv[curr] = left
        nxt[curr] = right

    result = list()
    
    for _ in range(M):
        cmd = next(iterator)
        
        if cmd == 'BN':
            i = int(next(iterator))
            j = int(next(iterator))
            
            k = nxt[i]
            result.append(k)
            nxt[i] = j
            prv[j] = i
            nxt[j] = k
            prv[k] = j
            
        elif cmd == 'BP':
            i = int(next(iterator))
            j = int(next(iterator))
            
            k = prv[i]
            result.append(k)
            nxt[k] = j
            prv[j] = k
            nxt[j] = i
            prv[i] = j
            
        elif cmd == 'CN':
            i = int(next(iterator))
            
            target = nxt[i]
            k = nxt[target]
            result.append(target)
            nxt[i] = k
            prv[k] = i
            
        elif cmd == 'CP':
            i = int(next(iterator))
            
            target = prv[i]
            k = prv[target]
            result.append(target)        
            nxt[k] = i
            prv[i] = k

    print('\n'.join(map(str, result)))

if __name__ == '__main__':
    solve()