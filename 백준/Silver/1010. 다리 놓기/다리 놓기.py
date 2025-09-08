import sys

def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def combination(n, m):
    # mCn = m! / n! * (m - n)!
    combination = factorial(m) // (factorial(n) * factorial(m - n))
    return combination

case_count = int(sys.stdin.readline().strip())
answer = list()
for _ in range(0, case_count):
    n, m = map(int, sys.stdin.readline().strip().split())
    answer.append(combination(n, m))

for _ in answer:
    print(_)