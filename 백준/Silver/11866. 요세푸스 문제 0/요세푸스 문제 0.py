import sys

N, K = map(int, sys.stdin.readline().strip().split())
queue = list()
for i in range(1, N + 1):
    queue.append(i)

joseputh = list()
current_index = 0
while len(joseputh) < N:
    current_len = len(queue)
    current_index += K - 1
    if current_index >= current_len:
        current_index %= current_len
    joseputh.append(queue[current_index])
    del queue[current_index]

print('<', end='')
for i in range(N - 1):
    print(joseputh[i], end=', ')
print(joseputh[N - 1], end='')
print('>')