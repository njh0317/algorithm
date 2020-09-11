N,K = map(int, input().split())
count = 0

# count+=N%K

# N=N-N%K

while(True):
    if N == 1:
        break
    if(N%K!=0):
        count+=1
        N=N-1
    else:
        N = N // K
        count+=1


print(count)
