N, K = map(int, input().split())
arr = []
visited = []
horse = []
dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

def rotate(num):
    if(num == 1):
        return 2
    elif(num == 2):
        return 1
    elif(num == 3):
        return 4
    elif(num == 4):
        return 3
def isIn(nowx, nowy):
    if(0>nowx or nowx>=N or 0>nowy or nowy>=N or arr[nowy][nowx] == 2):
        return False
    return True

def startgame():
    turn = 0
    flag = 0
    while(True):
        if(flag == 1):
            return turn
        if(turn>1000):
            return -1
        turn+=1
        for i in range(len(horse)):
            y,x,d = horse[i][0], horse[i][1], horse[i][2]
            horse_situ = visited[y][x]
            change_horse = horse_situ[horse_situ.index(i+1):]
            #horse_situ = horse_situ[:horse_situ.index(i+1)]
            nextx = x+dx[d]
            nexty = y+dy[d]
            if(isIn(nextx, nexty)):
                for j in change_horse: #모두 위치 이동
                    horse[j-1][0] = nexty
                    horse[j-1][1] = nextx
                visited[y][x] = visited[y][x][:horse_situ.index(i + 1)]
                if(arr[nexty][nextx] == 0):#이동 하려고 하는 곳이 흰색 일때
                    visited[nexty][nextx]+=change_horse

                elif(arr[nexty][nextx] == 1):#이동 하려고 하는 곳이 빨간색 일때
                    change_horse.reverse()
                    visited[nexty][nextx]+=change_horse
                if (len(visited[nexty][nextx]) >= 4):
                    flag = 1
                    break

            else: #파란색이거나 경계를 벗어나는 경우
                d = rotate(d)
                nextx = x+dx[d]
                nexty = y+dy[d]
                horse[i][2] = d
                if(isIn(nextx, nexty)):
                    for j in change_horse:  # 모두 위치 이동
                        horse[j-1][0] = nexty
                        horse[j-1][1] = nextx
                    visited[y][x] = visited[y][x][:horse_situ.index(i + 1)]
                    if (arr[nexty][nextx] == 0):  # 이동 하려고 하는 곳이 흰색 일때
                        visited[nexty][nextx] += change_horse

                    elif (arr[nexty][nextx] == 1):  # 이동 하려고 하는 곳이 빨간색 일때
                        change_horse.reverse()
                        visited[nexty][nextx] += change_horse
                    if (len(visited[nexty][nextx]) >= 4):
                        flag = 1
                        break


for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    new_list = []
    for j in range(N):
        new_list.append([])
    visited.append(new_list)

for i in range(K):
    y, x, d = map(int, input().split())
    horse.append([y-1,x-1,d])
    visited[y-1][x-1].append(i+1)

print(startgame())