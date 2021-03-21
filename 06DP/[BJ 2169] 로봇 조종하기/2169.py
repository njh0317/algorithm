import sys
sys.setrecursionlimit(10**4)
dx = [-1, 0, 1] #왼오아
dy = [0, 1, 0]
def isin(y, x):
    if(0<=y<N and 0<=x<M):
        return True

    return False
def robot(y, x, before_index):
    if(y == N-1 and x == M-1):
        return arr[y][x]
    if(visited[y][x][before_index]!=-1):
        return visited[y][x][before_index]
    visited[y][x][before_index] = arr[y][x]
    max_cost = -100001
    for i in range(3):
        nexty, nextx = y+dy[i], x+dx[i]
        if(isin(nexty, nextx) and abs(i-before_index)!=2):
            max_cost = max(max_cost,robot(nexty, nextx, i))
    visited[y][x][before_index]+=max_cost
    return visited[y][x][before_index]

if __name__ == "__main__":
    N, M = map(int, input().split())
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            visited[i][j] = [-1, -1, -1]

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    print(robot(0,0,1))
