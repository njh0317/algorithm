dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
def isin(y, x):
    if(0<=y<N and 0<=x<N):
        return True
    return False
def init():
    cloud = []
    #(N, 1), (N, 2), (N-1, 1), (N-1, 2)
    cloud.append([N-1, 0])
    cloud.append([N-1, 1])
    cloud.append([N-2, 0])
    cloud.append([N-2, 1])
    return cloud
def move_cloud(d, s, cloud):
    for i in range(len(cloud)):
        y, x = cloud[i]
        nexty, nextx = (y+dy[d]*(s%N)+N)%N, (x+dx[d]*(s%N)+N)%N
        cloud[i] = [nexty, nextx]
    return

def start():
    cloud = init()
    for i in range(M):
        d, s = map(int, input().split())
        move_cloud(d, s, cloud)
        visited = [[False]*N for _ in range(N)]
        for k in cloud:
            y, x = k
            arr[y][x]+=1
            visited[y][x] = True
        cloud = []
        plus = []
        for y in range(N):
            for x in range(N):
                if visited[y][x]:
                    cnt = 0
                    for d in range(2, 9, 2):
                        ny, nx = y+dy[d], x+dx[d]
                        if(isin(ny, nx) and arr[ny][nx]>0):
                            cnt+=1
                    plus.append([y, x, cnt])
                else:
                    if(arr[y][x]>=2):
                        cloud.append([y, x])
        for k in plus:
            y, x, cnt = k
            arr[y][x] += cnt
        for k in cloud:
            y, x = k
            arr[y][x] -= 2
    return
if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    start()
    answer = 0
    for i in arr:
        answer+=sum(i)
    print(answer)