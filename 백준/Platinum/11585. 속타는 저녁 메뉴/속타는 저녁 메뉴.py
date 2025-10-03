import sys

N = int(input())
pattern = list(sys.stdin.readline().strip().split())
current = list(sys.stdin.readline().strip().split())
string = current * 2
string.pop()

if all(x == pattern[0] for x in pattern):
    print('1/1')
    exit(0)


failure = [-1] * N # failure 함수
failure[0] = 0
j = 0
for i in range(1, N):
    while j > 0 and pattern[i] != pattern[j]:
        j = failure[j - 1]
    if pattern[i] == pattern[j]:
        j += 1
    failure[i] = j
# print(failure) for Debugging

# pattern matching
i = 0
j = 0
count = 0
lens = len(string)
lenp = len(pattern)
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

# count / N 을 기약분수로 나타내기
def gcd(count, N):
    while count != 0:
        N, count = count, N % count
    return N

print(count // gcd(count, N), '/', N // gcd(count, N), sep='')