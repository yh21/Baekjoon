import sys

input = sys.stdin.read

def solve():
    data = input().split()
    
    if not data:
        return

    iterator = iter(data)
    
    N = int(next(iterator))
    K = int(next(iterator))
    arr = list(range(1, N + 1))
    
    for _ in range(K):
        A = int(next(iterator))
        B = int(next(iterator))
        C = int(next(iterator))
        
        cut_segment = arr[A-1 : B]
        del arr[A-1 : B]
        arr[C:C] = cut_segment

    for num in arr[:10]:
        print(num)

if __name__ == '__main__':
    solve()