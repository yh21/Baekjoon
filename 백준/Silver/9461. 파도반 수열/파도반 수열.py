# f(n) = f(n - 1) + f(n - 5)
import sys

t = int(sys.stdin.readline().strip())
n_list = list()

def func(n):
    test_list = [1, 1, 1, 2, 2]
    for _ in range(0, 100):
        test_list.append(-1)
    for i in range(5, n):
        test_list[i] = test_list[i - 1] + test_list[i - 5]
    return test_list[n - 1]

for _ in range(0, t):
    n_list.append(int(sys.stdin.readline().strip()))

for num in n_list:
    print(func(num))