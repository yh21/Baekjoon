import sys

n = int(sys.stdin.readline().strip())
stack = list()

test_case = list()
for _ in range(0, n):
    operation = list(map(int, sys.stdin.readline().strip().split()))
    test_case.append(operation)

for i in range(0, n):
    if len(test_case[i]) != 1:
        stack.append(test_case[i][1])
    if test_case[i][0] == 2:
        if len(stack) != 0:
            print(stack[len(stack) - 1])
            stack.pop()
        else:
            print(-1)
    if test_case[i][0] == 3:
        print(len(stack))
    if test_case[i][0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if test_case[i][0] == 5:
        if len(stack) != 0:
            print(stack[len(stack) - 1])
        else:
            print(-1)