n = int(input())
original_score = list(map(int, input().split()))
max_score = max(original_score)
new_score = list()

for i in range(0, n):
    new_score.append((original_score[i] / max_score) * 100)

total = 0
for i in range(0, n):
    total+= new_score[i]

print(total / n)