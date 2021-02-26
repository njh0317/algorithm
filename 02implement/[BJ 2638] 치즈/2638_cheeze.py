dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
cheeze_num = 0
def isin(y, x):
    if(0<=y<N and 0<=x<M):
        return True
    return False
def removecheeze():
    time = 0
    global cheeze_num
    while(cheeze_num>0):
        #1)2변 이상이 공기와 접촉 확인
        delete_list = []#y, x
        for y in range(N):
            for x in range(M):
                if(arr[y][x] == 1):
                    air = 0
                    for i in range(4):
                        nextx = x+dx[i]
                        nexty = y+dy[i]
                        if(isin(nexty, nextx)):
                            if(arr[nexty][nextx] == 2):
                                air+=1
                        else:
                            air+=1
                                # if(air>=2):
                                #     break
                    if(air>=2):#공기 접촉이 2이상이면 
                        delete_list.append([y, x])
                        
        #2)확인된 치즈 제거
        for cheeze in delete_list:
            cheeze_y, cheeze_x = cheeze
            arr[cheeze_y][cheeze_x] = 2
        #3)내부 공기-외부공기 접촉 확인
        visited_contact = [[False]*M for _ in range(N)]
        for y in range(N):
            for x in range(M):
                if(arr[y][x]==0 and visited_contact[y][x] == False):#내부공기이고 
                    for i in range(4):
                        nexty = y+dy[i]
                        nextx = x+dx[i]
                        if(isin(nexty, nextx)):
                            if arr[nexty][nextx] == 2:#주변에 외부공기가 있으면 
                                checkair(y, x, 2, visited_contact)#4)외부 공기로 변환 
                                break
                        else:
                            checkair(y, x, 2, visited_contact)#4)외부 공기로 변환 
                            break
        time+=1
        cheeze_num-=len(delete_list)
    return time
def checkair(y, x, air_num, visited):
    #BFS
    queue = []
    queue.append([y, x])
    visited[y][x] = True
    arr[y][x] = air_num
    while(queue):
        nowy, nowx = queue.pop(0)
        for i in range(4):
            nexty = nowy + dy[i]
            nextx = nowx + dx[i]
            if(isin(nexty, nextx)):
                if(visited[nexty][nextx] == False and arr[nexty][nextx]==0):
                    visited[nexty][nextx] = True
                    arr[nexty][nextx] = air_num
                    queue.append([nexty, nextx])
    return

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    visited_air = [[False]*M for _ in range(N)]

    #가장자리 부분 확인 
    flag = False
    cheeze_num = 0
    for i in range(N):
        for j in range(M):
            if(arr[i][j] == 1):
                cheeze_num+=1
            if(flag == False and (i==0 or j == 0 or i == N-1 or j == M-1)):#가장자리면 
                if(visited_air[i][j] == False and arr[i][j] == 0):
                    checkair(i, j, 2, visited_air)
                    flag = True
    print(removecheeze())

