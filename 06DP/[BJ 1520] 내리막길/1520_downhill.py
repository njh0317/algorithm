import sys
sys.setrecursionlimit(100000)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
M, N = map(int, input().split())
flag = [[-1]*N for _ in range(M)]
num = 0
def find_downhill(road, x, y):
    if(x == N-1 and y == M-1):
        return 1
    if(flag[y][x]!=-1): #방문한 적이 있다면
        return flag[y][x]
    flag[y][x] = 0 #방문 표시
    for i in range(0, 4):
        nextX = x + dx[i]
        nextY = y + dy[i]

        if(nextX>=0 and nextY>=0 and nextX<N and nextY < M):
            if(road[nextY][nextX]<road[y][x]):
                flag[y][x] += find_downhill(road, nextX, nextY)

    return flag[y][x]
    


road = []
for i in range(M):
    road.append(list(map(int, input().split())))


find_downhill(road, 0, 0)
print(flag[0][0])


