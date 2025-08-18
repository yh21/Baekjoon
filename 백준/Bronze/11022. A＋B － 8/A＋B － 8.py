import sys

n = int(input())
test_case = list()
for _ in range(0, n):
    a, b = map(int, sys.stdin.readline().strip().split())
    test_case.append((a, b))

for i in range(0, n):
    print("Case #", i + 1, ': ', test_case[i][0], ' + ', test_case[i][1], ' = ', test_case[i][0] + test_case[i][1], sep = '')