import sys
import collections
sys.setrecursionlimit(100000)
Input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def isin(y, x):
    if(0<=y<N and 0<=x<M):
        return True
    return False

def bfs(y, x, visited):
    arr2 = [item[:] for item in arr]
    queue = collections.deque([[y, x]])
    visited[y][x] = True
    while(queue):
        nowy, nowx = queue.popleft()
        for i in range(4):
            nexty = nowy + dy[i]
            nextx = nowx + dx[i]
            if(isin(nexty, nextx)):
                if(arr2[nexty][nextx]==0):
                    if(arr[nowy][nowx]>0):
                        arr[nowy][nowx]-=1
                if(arr2[nexty][nextx]>0 and visited[nexty][nextx] == False):
                    visited[nexty][nextx] = True
                    queue.append([nexty, nextx])
    return

def start():
    time = 0
    while(True):
        visited = [[False]*M for _ in range(N)]     
        island = 0 
        flag = False
        for i in range(N):
            for j in range(M):
                if(arr[i][j]>0 and visited[i][j] == False):
                    if(island>0):
                        print(time)
                        sys.exit()   
                    bfs(i, j, visited)
                    flag = True
                    island+=1 
        if(flag == False):
            print(0)
            sys.exit()
        time+=1   
    return time
if __name__ == "__main__":
    N, M = map(int, Input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, Input().split())))
    start()