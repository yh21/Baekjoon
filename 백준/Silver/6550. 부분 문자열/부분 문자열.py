import sys

data = sys.stdin.read().strip().split('\n')
for line in data:
    a, b = list(line.split())
    pattern = list(a)
    message = list(b)

    i = 0
    for j in range(len(message)):
        if pattern[i] == message[j]:
            i += 1
        if i == len(pattern):
            break

    if i == len(pattern):
        print('Yes')
    else:
        print('No')