import sys

string = list(sys.stdin.readline().rstrip())
# print(string) for Debugging
pattern = list(sys.stdin.readline().rstrip())
# print(pattern)
lens = len(string)
lenp = len(pattern)

# failure function
failure = [0] * lenp
j = 0
for i in range(1, lenp):
    while j > 0 and pattern[i] != pattern[j]:
        j = failure[j - 1]
    if pattern[i] == pattern[j]:
        j += 1
    failure[i] = j
# print(failure) for Debugging

count = 0
bucket = list()

# pattern matching
i = 0
j = 0
while i < lens:
    if string[i] == pattern[j]:
        i += 1
        j += 1
        if j == lenp:
            count += 1
            bucket.append(i + 1 - lenp)
            j = failure[j - 1]
    elif j == 0:
        i += 1
    else:
        j = failure[j - 1]

print(count)
for index in bucket:
    print(index, end=' ')