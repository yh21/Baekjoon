import sys

n = int(sys.stdin.readline().strip())
num_list = list()

while n != 0:
    num_list.append(n % 10)
    n = n // 10

# print(num_list)

num_list.sort(reverse=True)
for i in range(0, len(num_list)):
    print(num_list[i], end='')