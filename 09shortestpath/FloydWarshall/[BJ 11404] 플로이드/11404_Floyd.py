INF = 10000001
def floyd():
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if(j!=k):
                    bus[j][k] = min(bus[j][k],bus[j][i] + bus[i][k])
    
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    bus = [[INF]*(n+1) for _ in range(n+1)]

    for i in range(m):
        start, end, money = map(int, input().split())
        bus[start][end] = min(bus[start][end], money)
    floyd()
    for i in range(1, n+1):
        for j in range(1, n+1):
            if(bus[i][j]==INF):
                print(0, end=" ")
            else:
                print(bus[i][j], end=" ")
        print()