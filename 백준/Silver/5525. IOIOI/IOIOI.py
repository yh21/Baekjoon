import sys

N = int(input())
M = int(input())
string = list(sys.stdin.readline().strip())
pattern = ['I', 'O'] * N + ['I']
lens = len(string)
lenp = len(pattern)

# failure function
failure = [0] * lenp
j = 0
for k in range(1, lenp):
    while j > 0 and pattern[k] != pattern[j]:
        j = failure[j - 1]
    if pattern[k] == pattern[j]:
        j += 1
    failure[k] = j

i = 0
j = 0
count = 0
while i < lens:
    if string[i] == pattern[j]:
        i += 1
        j += 1
        if j == lenp:
            count += 1
            j = failure[j - 1]
    elif j == 0:
        i += 1
    else:
        j = failure[j - 1]

print(count)