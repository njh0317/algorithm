N = int(input())
score = []
for i in range(N):
    score.append(int(input()))

max_score = [score[0]]
if(N>1):
    if(N >= 2):
        max_score.append(score[0]+score[1])
        
    if(N >= 3):
        max_score.append(max(score[0]+score[2], score[1]+score[2]))
        for i in range(3, N):
            max_score.append(score[i]+max(score[i-1]+max_score[i-3], max_score[i-2]))
print(max_score[N-1])


