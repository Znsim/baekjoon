N = int(input())
score = list(map(int,input().split()))
max_score = max(score)

total = 0
for i in range(N) :
    new = score[i]/max_score * 100
    total += new

print(total/N)
