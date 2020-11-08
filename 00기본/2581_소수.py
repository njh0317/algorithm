N = int(input())
M = int(input())

arr = [True]*(M+1)


for i in range(2, int(M**0.5)+1):
    if(arr[i]==0):
        continue
    for j in range(i+i, M+1, i):
        arr[j] = False
sum_num=0
flag = 0
for j in range(N, M+1):
    if(j == 1):
        continue
    if(arr[j]):
        if(flag==0):
            flag = j
        sum_num+=j
if(flag == 0):
    print(-1)
else:
    print(sum_num)
    print(flag)