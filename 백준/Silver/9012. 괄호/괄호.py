import sys

n = int(input())
message = list()
for i in range(0, n):
    line = sys.stdin.readline().strip()
    chars = list(line)
    message.append(chars)

for i in range(0, n):
    stack = list()
    length = len(message[i])
    for j in range(0, length):
        if message[i][j] == '(':
            stack.append(0)
        else:
            if len(stack) == 0:
                print('NO')
                break
            stack.pop()
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')