import sys

n = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().strip().split()))
# print(num_list)
num_list.sort()

forward = 0
back = len(num_list) - 1

x = int(sys.stdin.readline().strip())
count = 0

while forward < back:
    if num_list[forward] + num_list[back] == x:
        count += 1
        forward += 1
        back -= 1
    elif num_list[forward] + num_list[back] < x:
        forward += 1
    elif num_list[forward] + num_list[back] > x:
        back -= 1
    
print(count)