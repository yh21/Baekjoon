import sys

N, M = map(int, sys.stdin.readline().strip().split())
PCS = list()
EA = list()
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    PCS.append(a)
    EA.append(b)

share = N // 6
mod = N % 6

min_PCS = min(PCS)
min_EA = min(EA)

if min_EA * 6 <= min_PCS:
    print(N * min_EA)
elif min_EA * mod <= min_PCS:
    print(min_PCS * share + min_EA * mod)
else:
    print(min_PCS * (share + 1))