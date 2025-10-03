import sys

bucket = list()
while True:
    string = list(sys.stdin.readline().strip())
    if len(string) == 1 and string[0] == '.':
        break
    bucket.append(string)
# print(bucket) for Debugging

for i in range(len(bucket)):
    lens = len(bucket[i])

    # failure function
    failure = [-1] * lens
    failure[0] = 0
    j = 0
    for k in range(1, lens):
        while j > 0 and bucket[i][k] != bucket[i][j]:
            j = failure[j - 1]
        if bucket[i][k] == bucket[i][j]:
            j += 1
        failure[k] = j
    # print(failure) for debugging
    
    # failure period
    period = lens - failure[lens - 1]
    if lens % period != 0:
        print(1)
    else:
        print(lens // period)