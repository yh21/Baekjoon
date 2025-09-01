import sys

N = int(sys.stdin.readline().strip())
stack = list()

for i in range(0, N):
    func = sys.stdin.readline().strip().split()
    if len(func) != 1:
        func[1] = int(func[1])
    if func[0] == 'push':
        stack.append(func[1])
    if func[0] == 'pop':
        if len(stack) != 0:
            print(stack[len(stack) - 1])
            stack.pop()
        else:
            print(-1)
    if func[0] == 'size':
        print(len(stack))
    if func[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if func[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])