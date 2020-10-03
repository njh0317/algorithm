import sys
sys.setrecursionlimit(10**9)
dx = [-1,0,1,1,1,0,-1,-1]
dy = [-1,-1,-1,0,1,1,1,0]
visited = []
def dfs(x,y,flag,w,h):
    visited[y][x] = 1

    for i in range(8):
        nextX = x+dx[i]
        nextY = y+dy[i]

        if(nextX>=0 and nextY>=0 and nextX<w and nextY<h):
            if(flag[nextY][nextX] == 1 and visited[nextY][nextX] == 0):
                dfs(nextX, nextY, flag, w, h)
    
    return

if __name__ == "__main__":

    flag_num = 0
    h, w = map(int,sys.stdin.readline().split()) #너비 w 높이 h
    flag = []
    visited = [[0]*w for _ in range(h)]
    for i in range(h):
        flag.append(list(map(int,sys.stdin.readline().split())))
    for i in range(h):
        for j in range(w):
            if(flag[i][j]==1 and visited[i][j]==0):
                flag_num+=1
                dfs(j,i,flag, w,h)
        
    print(flag_num)
