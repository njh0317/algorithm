import collections
dx = [0, 0, 1, 0, 0, -1]
dy = [0, -1, 0, 0, 1, 0]
dz = [-1, 0, 0, 1, 0, 0]
day = -1
def isin(z, y, x):
    if(0<=z<H and 0<=y<N and 0<=x<M):
        return True
    return False
def bfs():
    queue = collections.deque([])
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if(tomato_map[h][i][j] == 1):
                    queue.append([h, i, j])
                    visited[h][i][j] = 0
                    global day
                    day = 0
        
    while(queue):
        nowz, nowy, nowx = queue.popleft()
        for i in range(6):
            nextz = nowz + dz[i]
            nexty = nowy + dy[i]
            nextx = nowx + dx[i]
            if(isin(nextz, nexty, nextx)):
                if(tomato_map[nextz][nexty][nextx] == 0 and visited[nextz][nexty][nextx] == -1):
                    visited[nextz][nexty][nextx] = visited[nowz][nowy][nowx] + 1
                    day = max(day, visited[nextz][nexty][nextx])
                    queue.append([nextz, nexty, nextx])
if __name__ == "__main__":
    M, N, H = map(int, input().split())
    tomato_map = []
    visited = [[[-1]*M for _ in range(N)] for _ in range(H)]
    for h in range(H):
        box = []
        for n in range(N):
            now_list = list(map(int, input().split()))
            for m in range(M):
                if(now_list[m] == -1):
                    visited[h][n][m] = 0
            box.append(now_list)
        tomato_map.append(box)
    bfs()
    flag =  True
    for i in visited:
        for j in i:
            if(-1 in j):
                flag = False
                break
        if(flag == False):
            break
    if(flag == False):
        print(-1)
    else:
        print(day)

