import sys

N = int(input())
string = list(sys.stdin.readline().strip())

func = [-1] * N # failure 함수
func[0] = 0
j = 0
for i in range(1, N):
    while j > 0 and string[i] != string[j]:
        j = func[j - 1]
    if string[i] == string[j]:
        j += 1
    func[i] = j
# print(func) for Debugging

k = N - func[N - 1]
print(k)