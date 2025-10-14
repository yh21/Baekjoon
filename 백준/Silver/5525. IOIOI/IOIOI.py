import sys

N = int(input())
M = int(input())
string = list(sys.stdin.readline().strip())
pattern = ['I', 'O'] * N + ['I']
lens = len(string)
lenp = len(pattern)
# print(pattern) for Debugging

count = 0
for i in range(lens - lenp + 1):
    j = 0
    while j < lenp:
        if string[i + j] == pattern[j]:
            j += 1
        else:
            break
    if j == lenp:
        count += 1
    
print(count)