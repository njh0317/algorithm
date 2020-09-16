from collections import deque
dx = [-1,0,1,0]
dy = [0,-1,0,1]
N, M = map(int, input().split())
maze = []


def findload(x,y):
    queue = deque()
    queue.append((x,y))
    while(queue):
        w,v = queue.popleft()
        for i in range(0,4):
            nextx = w+dx[i]
            nexty = v+dy[i]
            if(nextx>=0 and nexty>=0 and nextx<N and nexty<M):
                if(maze[nextx][nexty]==1):#처음방문하는경우
                    queue.append((nextx,nexty))
                    maze[nextx][nexty]+=maze[w][v]



for i in range(0, N):
    maze.append(list(map(int, input())))

findload(0,0)
print(str(maze[N-1][M-1]))
