N = int(input())
work = []
money = [0 for _ in range(N+1)]
for i in range(N):
    work.append(list(map(int, input().split())))

for i in range(N-1, -1, -1):
    if(work[i][0]+i>N):
        continue
    money[i] = max(money[i+work[i][0]:])+work[i][1]


print(max(money))