import sys

infix = list(sys.stdin.readline().strip())
stack = list()
oper = ['+', '-', '*', '/', '(', ')']
isp = [12, 12, 13, 13, 0, 19]
icp = [12, 12, 13, 13, 20, 19]
leni = len(infix)

for i in range(leni):
    if infix[i] not in oper:
        print(infix[i], end='')
    elif infix[i] == ')':
        while stack[len(stack) - 1] != '(':
            print(stack[len(stack) - 1], end='')
            stack.pop()
        stack.pop()
    else:
        if len(stack) == 0:
            stack.append(infix[i])
        else:
            while isp[oper.index(stack[len(stack) - 1])] >= icp[oper.index(infix[i])]:
                print(stack[len(stack) - 1], end='')
                stack.pop()
                if len(stack) == 0:
                    break
            stack.append(infix[i])

stack.reverse()
for operation in stack:
    print(operation, end='')