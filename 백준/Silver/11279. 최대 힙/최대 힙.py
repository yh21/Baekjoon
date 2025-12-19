import sys
import heapq
input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    nums = data[1:]
    
    heap = []
    results = []

    for i in range(N):
        n = int(nums[i])
        
        if n == 0:
            if not heap:
                results.append("0")
            else:
                results.append(str(-heapq.heappop(heap)))
        else:
            heapq.heappush(heap, -n)
        
    sys.stdout.write("\n".join(results) + "\n")

solve()