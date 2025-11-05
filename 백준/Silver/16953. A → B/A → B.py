N, K = map(int, input().split())
count = 0

while True:
    if int(str(K)[-1]) == 3 or int(str(K)[-1]) == 5 or int(str(K)[-1]) == 7 or int(str(K)[-1]) == 9:
        print(-1)
        exit(0)
    elif int(str(K)[-1]) == 1:
        K = int(str(K)[0:-1])
    else:
        K //= 2
    count += 1

    if N == K:
        print(count + 1)
        exit(0)
    if N > K:
        print(-1)
        exit(0)