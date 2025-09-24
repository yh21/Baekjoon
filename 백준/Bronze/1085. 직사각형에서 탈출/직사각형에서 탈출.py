import sys

x, y, w, h = map(int, sys.stdin.readline().strip().split())
smallest = min(x, y, w - x, h - y)
print(smallest)