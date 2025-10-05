import sys

def func(A, B, C):
    if B == 0:
        return 1
    elif B % 2 == 0:
        return (func(A, B // 2, C) ** 2) % C
    else:
        return ((func(A, B // 2, C) ** 2) * A) % C

A, B, C = map(int, sys.stdin.readline().strip().split())
print(func(A, B, C))