import sys

k = int(input())
command = list()
stack = list()

for i in range(0, k):
    num = int(sys.stdin.readline())
    command.append(num)

for cmd in command:
    if cmd == 0:
        stack.pop()
    else:
        stack.append(cmd)

len = len(stack)
total = 0
for i in range(0, len):
    total += stack[i]

print(total)