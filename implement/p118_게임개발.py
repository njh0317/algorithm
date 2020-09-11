dy = [-1,0,1,0]
dx = [0,1,0,-1]

N, M = map(int,input().split())
nowX, nowY, nowsight = map(int,input().split())
arr = []
flag = []
for i in range(0, N):
    arr.append(list(map(int,input().split())))
    arrx = []
    for j in range(0, M):
        arrx.append(0)
    flag.append(arrx)
turn_time = 0
num = 1
flag[nowY][nowX] = 1
sight = nowsight 
while(True):
    sight = sight-1
    if(sight == -1):
        sight = 3
    nextX = nowX+dx[sight]
    nextY = nowY+dy[sight]
    if not (nextX<0 or nextY<0 or nextX >= M or nextY >= N):
        if(arr[nextY][nextX]==0 and flag[nextY][nextX]==0):
            nowX = nextX
            nowY = nextY
            num+=1
            turn_time = 0
            flag[nowY][nowX]=1
        else:
            turn_time +=1
    else:
        turn_time+=1

    if(turn_time == 4):
        back = (sight+1)%4
        nextX = dx[back]
        nextY = dy[back]
        if(arr[nextY][nextX]==1):
            break
        else:
            nowX = nextX
            nowY = nextY
            turn_time=0

print(num)

        

    