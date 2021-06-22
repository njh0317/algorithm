dx = [-1, -1, 0]
dy = [0, -1, -1]
def isin(y, x):
    if 0<=y<N and 0<=x<M:
        return True
    return False
if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = []

    for i in range(N):
        newdp = []
        for j in range(M):
            newdp.append(-1)
        dp.append(newdp)
    
    for y in range(N):
        for x in range(M):
            nownum = 0
            for k in range(3):
                beforey, beforex = y+dy[k], x+dx[k]
                if isin(beforey, beforex):
                    nownum = max(nownum, dp[beforey][beforex])
            dp[y][x] = nownum+arr[y][x]
    
    print(dp[N-1][M-1])

