import sys

string, K = sys.stdin.readline().strip().split()
string = list(string)
K = int(K)
lens = len(string)

# failure function
failure = [0] * lens
j = 0
for k in range(1, lens):
    while j > 0 and string[k] != string[j]:
        j = failure[j - 1]
    if string[k] == string[j]:
        j += 1
    failure[k] = j

# answer
R = lens - failure[lens - 1]
print(lens + (K - 1) * R)