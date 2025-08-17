import sys

n = int(input())
num = list()

for _ in range(0, n):
    number = int(sys.stdin.readline().strip())
    num.append(number)

num.sort()

for i in range(0, n):
    print(num[i])