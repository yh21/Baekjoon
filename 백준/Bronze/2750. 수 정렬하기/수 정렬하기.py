n = int(input())

num = list()
for i in range(0, n):
    num.append(int(input()))

num.sort()

for x in num:
    print(x)