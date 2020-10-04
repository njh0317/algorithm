import sys
dr = [1,0,-1,0] #행
dc = [0,-1,0,1] #열 하, 좌, 상, 우

R, C, T = map(int,sys.stdin.readline().split())#R = 행, C = 열, T = 시간
room  = []
visited = []
def spread2():
    visited = [[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if(room[i][j]>=5):
                dust = room[i][j]//5
                for k in range(4):
                    nextR = i + dr[k]
                    nextC = j + dc[k]
                    if(nextR<R and nextC<C and nextR>=0 and nextC>=0 and room[nextR][nextC]!=-1):
                        room[i][j]-=dust
                        visited[nextR][nextC]+=dust
    
    for i in range(R):
        for j in range(C):
            room[i][j]+=visited[i][j]


def spread(r, c, spread_dust): #재귀로 짠 것
    visited[r][c]=1 #방문 표시해주고
    num = 0
    dust = room[r][c]//5
    if(dust == 0):
        room[r][c]+=spread_dust
        return 0
    for i in range(4):
        nextR = r + dr[i]
        nextC = c + dc[i]
        if(nextR<R and nextC<C and nextR>=0 and nextC>=0):
            if(room[nextR][nextC] > -1):
                num+=1 # spread 되는 공간의 수 세아려줌
                if (room[nextR][nextC]!=0 and visited[nextR][nextC]==0): # 퍼지려는 공간에 이미 미세먼지가 있다면
                    spread(nextR, nextC, dust) # 받은 미세먼지 양을 더해줌
                else: 
                    room[nextR][nextC] += dust
                    visited[nextR][nextC] = 1 #방문 표시해줌
    room[r][c]+=spread_dust
    room[r][c]-=num*dust
    return dust
def start_machine(r, c, option):
    dust = 0
    nextdust = 0
    start = 3
    nowR = r + dr[start]
    nowC = c + dc[start]
    if(option == 0):#반시계방향, 윗쪽
        while(True):
            if(r == nowR and c == nowC): #다시 원위치이면 끝
                break
            nextdust = room[nowR][nowC] #현재 값을 저장해주고
            room[nowR][nowC] = dust # 이전 값을 저장해주고
            dust = nextdust
            if((nowC == C-1 and nowR == r) or (nowC == C-1 and nowR == 0) or (nowC == 0 and nowR == 0)):
                start -= 1
            nowR += dr[start]
            nowC += dc[start]
    if(option == 1):#시계방향, 아래쪽
        while(True):
            if(r == nowR and c == nowC): #다시 원위치이면 끝
                break
            nextdust = room[nowR][nowC] #현재 값을 저장해주고
            room[nowR][nowC] = dust # 이전 값을 저장해주고
            dust = nextdust
            if((nowC == C-1 and nowR == r) or (nowC == C-1 and nowR == R-1) or (nowC == 0 and nowR == R-1)):
                start = (start + 1)%4
            nowR += dr[start]
            nowC += dc[start]
def print_room():
    for i in room:
        print(i)
    print()
        
if __name__ == "__main__":
    machine = []
    for i in range(R):
        new_room = list(map(int, sys.stdin.readline().split()))
        if(-1 in new_room):
            machine.append([i,0])
        room.append(new_room)
    
    for t in range(T):        
        spread2()
        for i in range(2):
            start_machine(machine[i][0],machine[i][1],i)
    sum=0
    for i in range(R):
        for j in range(C):
            if(room[i][j]!=-1):
                sum+=room[i][j]
    print(sum)





     