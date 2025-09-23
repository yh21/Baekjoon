import sys

n = int(input())
peoples = list()
for i in range(0, n):
    age, name = sys.stdin.readline().strip().split()
    age = int(age)
    peoples.append((age, name))

peoples.sort(key = lambda x : x[0])

for age, name in peoples:
    print(age, name)