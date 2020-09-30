import sys
sys.setrecursionlimit(100000)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
M, N = map(int, input().split())
flag = [[-1]*N for _ in range(M)]
def find_route(x, y, road):
    if(x == N-1 and y == M-1):
        return 1
    if(flag[y][x]!=-1):
        return flag[y][x]
    
    flag[y][x]=0

    for i in range(4):
        nextx = x+dx[i]
        nexty = y+dy[i]

        if(nextx>=0 and nexty>=0 and nextx<N and nexty<M):
            if(road[nexty][nextx]<road[y][x]):
                flag[y][x]+=find_route(nextx, nexty, road)
        
    return flag[y][x]


road = []
for i in range(M):
    road.append(list(map(int, input().split())))

find_route(0, 0, road)
print(flag[0][0])




