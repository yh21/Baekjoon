import sys

x1, y1 = map(int, sys.stdin.readline().strip().split())
x2, y2 = map(int, sys.stdin.readline().strip().split())
x3, y3 = map(int, sys.stdin.readline().strip().split())

result = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)

if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)