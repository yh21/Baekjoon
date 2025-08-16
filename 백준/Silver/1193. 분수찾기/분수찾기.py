n = int(input())
i = 1
while n > i:
    n -= i
    i += 1

if i % 2 == 0:
    print(n, "/", i - n + 1, sep="")
else:
    print(i - n + 1, "/", n, sep="")