N = int(input())
num = []
for i in range(N):
    new_list = list(map(int, input().split()))
    num.append(new_list)

for i in range(1,N):
    for j in range(0, len(num[i])):
        if(j == 0):
            num[i][j] += num[i-1][0]
        elif(j == len(num[i])-1):
            num[i][j] += num[i-1][j-1]
        else:
            num[i][j] += max([num[i-1][j-1],num[i-1][j]])
print(max(num[N-1]))
            