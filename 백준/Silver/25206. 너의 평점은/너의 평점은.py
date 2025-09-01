import sys

credit = list()
score = list()
total_score = 0
for _ in range(0, 20):
    a, b, c = sys.stdin.readline().strip().split()
    b = float(b)
    if c == 'A+':
        c = 4.5
        total_score += b
    if c == 'A0':
        c = 4.0
        total_score += b
    if c == 'B+':
        c = 3.5
        total_score += b
    if c == 'B0':
        c = 3.0
        total_score += b
    if c == 'C+':
        c = 2.5
        total_score += b
    if c == 'C0':
        c = 2.0
        total_score += b
    if c == 'D+':
        c = 1.5
        total_score += b
    if c == 'D0':
        c = 1.0
        total_score += b
    if c == 'F':
        c = 0
        total_score += b
    if c == 'P':
        c = 0
    credit.append(b)
    score.append(c)

total = 0

for i in range(0, 20):
    total += credit[i] * score[i]

total = total / total_score
print(total)