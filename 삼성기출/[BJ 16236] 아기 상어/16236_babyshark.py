import sys
N = int(sys.stdin.readline())
di = [-1,0,0,1]
dj = [0,-1,1,0]
fsize = [0]*7
def bfs(arr,nowsize, ni, nj):
    visited = [[0]*N for _ in range(N)]
    queue = [[ni,nj,0]]
    visited[ni][nj] = 1
    besti = 9999
    bestj = 9999
    bestmove = 9999
    while(queue):
        vertex = queue.pop(0)
        for i in range(4):
            nexti = vertex[0]+di[i]
            nextj = vertex[1]+dj[i]
            if(vertex[2]+1>bestmove):
                return besti, bestj, bestmove
            if(nexti == -1 or nextj == -1 or nexti == N or nextj == N):
                continue
            if(visited[nexti][nextj]==1):
                continue
            if(arr[nexti][nextj]<nowsize and arr[nexti][nextj]!=0):
                if(besti>nexti): #같은 거리라면 윗쪽의 것을 먼저 선택해줌
                    besti = nexti
                    bestj = nextj
                    bestmove = vertex[2]+1
                elif(besti == nexti and bestj>nextj): # 같은 열에 위치하고 있으면 왼쪽 것을 먼저 선택해줌
                    besti = nexti
                    bestj = nextj
                    bestmove = vertex[2]+1

            if(visited[nexti][nextj]==0 and arr[nexti][nextj]<=nowsize):
                visited[nexti][nextj] = 1
                queue.append([nexti, nextj, vertex[2]+1])
    return -1, -1, -1

def find_shark(arr, now_size, eat_num, ni, nj):
    move = 0
    while(True):
        temp = 0
        check_size = now_size if now_size<=7 else 7
        for i in range(check_size-1, 0, -1):
            temp+=fsize[i]
        if(temp == 0): break
        nexti, nextj, nowmove = bfs(arr, now_size, ni, nj)
        if(nexti== -1 and nextj == -1 and nowmove == -1):
            return move
        fsize[arr[nexti][nextj]]-=1
        arr[nexti][nextj] = 9
        arr[ni][nj] = 0
        ni = nexti
        nj = nextj

        #움직인 이동거리 더해주기
        move+=nowmove

        #먹은 횟수 증가시킨 후 , 사이즈 변화 가능 여부 확인
        eat_num += 1
        if(now_size == eat_num):
            now_size+=1
            eat_num = 0
    return move


arr = []
starti = -1
startj = -1
for i in range(N):
    new_arr = list(map(int, sys.stdin.readline().split()))
    for j in new_arr:
        if(j==9):
            starti = i
            startj = new_arr.index(9)
        elif(j !=0):
            fsize[j]+=1
    arr.append(new_arr)

print(find_shark(arr, 2, 0, starti, startj))
