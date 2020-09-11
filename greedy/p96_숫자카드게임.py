N, M = map(int,input().split())
arr=[]
for i in range(0, N):
    arr.append(list(map(int,input().split())))


max_cardnum = -1

for i in range(0, N):
    # if(min(arr[i])>max_cardnum):
    #     max_cardnum = min(arr[i])
    max_cardnum=max(max_cardnum, min(arr[i]))

print(max_cardnum)