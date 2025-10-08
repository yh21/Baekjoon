import sys

L = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

suffix_array = [i for i in range(L)]
group = [ord(S[i]) for i in range(L)]

d = 1
while d < L:
    suffix_array.sort(key=lambda i: (group[i], group[i + d] if i + d < L else -1))
    new_group = [0] * L
    new_group[suffix_array[0]] = 0
    
    for i in range(1, L):
        prev = suffix_array[i - 1]
        curr = suffix_array[i]
        
        prev_key = (group[prev], group[prev + d] if prev + d < L else -1)
        curr_key = (group[curr], group[curr + d] if curr + d < L else -1)
        
        if prev_key != curr_key:
            new_group[curr] = new_group[prev] + 1
        else:
            new_group[curr] = new_group[prev]
            
    group = new_group

    if group[suffix_array[L-1]] == L - 1:
        break
        
    d *= 2

rank = [0] * L
for i in range(L):
    rank[suffix_array[i]] = i

lcp_array = [0] * L
k = 0

for i in range(L):
    if rank[i] == 0:
        continue
    if k > 0:
        k -= 1

    j = suffix_array[rank[i] - 1]
    while i + k < L and j + k < L and S[i + k] == S[j + k]:
        k += 1
        
    lcp_array[rank[i]] = k

answer = 0
if lcp_array:
    answer = max(lcp_array)

print(answer)