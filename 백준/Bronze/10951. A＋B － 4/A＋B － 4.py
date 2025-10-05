import sys

data = sys.stdin.read().strip().split('\n')
for line in data:
    a, b = map(int, line.split())
    print(a + b)