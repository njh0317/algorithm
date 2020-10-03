import sys
sys.setrecursionlimit(10**9)
N, M = map(int,sys.stdin.readline().split())
drawing = []
visited = [[0]*M for _ in range(N)]

for i in range(N):
    drawing.append(list(map(int,sys.stdin.readline().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfs(i, j, num):
    visited[i][j]=1 # 방문 표시
    for k in range(4):
        nexti = i+dy[k]
        nextj = j+dx[k]
        if (nexti !=-1 and nexti != N and nextj != -1 and nextj != M):
            if(drawing[nexti][nextj]==1 and visited[nexti][nextj] == 0):
                num = dfs(nexti,nextj,num+1)
    return num

big_drawing = 0
drawing_num = 0
for i in range(N):
    for j in range(M):
        if(drawing[i][j]==1 and visited[i][j] == 0):
            drawing_num+=1
            big_drawing = max(big_drawing,(dfs(i, j, 1)))
print(drawing_num)
print(big_drawing)

