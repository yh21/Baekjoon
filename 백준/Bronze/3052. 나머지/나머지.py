num = list()

for _ in range(0, 10):
    n = int(input()) % 42
    num.append(n)

test = list(set(num))

print(len(test))