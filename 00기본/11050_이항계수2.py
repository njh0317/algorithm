N, K = map(int, input().split())
multi = 1;
if(K == 0):
    print(int(multi))
else:
    for i in range(K):
        multi*=(N-i)
    for i in range(K, 0, -1):
        multi/=i
    print(int(multi))
