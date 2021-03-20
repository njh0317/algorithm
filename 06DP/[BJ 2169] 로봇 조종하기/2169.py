import sys
sys.setrecursionlimit(10**8)
dx = [-1, 1, 0] #왼오위
dy = [0, 0, -1]
def isin(y, x):
    if(0<=y<N and 0<=x<M):
        return True

    return False
def robot(y, x):
    if(visited[y][x]!=-1):
        return visited[y][x]
    if(y == 0 and x == 0):
        return arr[y][x]

    max_cost = 0
    for i in range(3):
        nexty, nextx = y+dy[i], x+dx[i]
        if(isin(nexty, nextx)):
            max_cost = max(max_cost,robot(nexty, nextx))
    visited[y][x]+=max_cost
    visited[y][x]+=arr[y][x]
    return visited[y][x]

if __name__ == "__main__":
    N, M = map(int, input().split())
    visited = [[-1]*M for _ in range(N)]
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    print(robot(N-1,M-1))