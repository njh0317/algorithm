import sys
N, K = map(int, sys.stdin.readline().split())


table = [[0 for _ in range(K+1)] for _ in range(N+1)]
max_num = 0
for i in range(1, N+1):
    weight, value = map(int, sys.stdin.readline().split())
    for j in range(1, K+1):
        
        if(j<weight):
            table[i][j] = table[i-1][j]
        else:
            table[i][j] = max(table[i-1][j], value+table[i-1][j-weight])

print(table[N][K])
