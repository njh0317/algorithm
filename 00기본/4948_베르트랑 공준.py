while(True):
    N = int(input())
    if(N==0):
        break
    M = N*2
    arr = [True]*(M+1)
    arr[1] = False

    for i in range(2, int(M**0.5)+1):
        if(arr[i]==0):
            continue
        for j in range(i+i, M+1, i):
            arr[j] = False
    print(arr[N+1:].count(True))
