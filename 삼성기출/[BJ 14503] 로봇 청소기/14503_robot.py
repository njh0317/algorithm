N, M = map(int, input().split())
r,c,d = map(int, input().split())
map1 = []
dr = [-1,0,1,0]
dc = [0,1,0,-1]
visited = [[True]*M for _ in range(N)]
def change_rotation(num):
    changenum = num-1
    if(changenum == -1):
        changenum = 3
    return changenum
def isInMap(nowr, nowc):
    if(0<=nowr<N and 0<=nowc<M and map1[nowr][nowc] == 0): #벽이 아니고 map 을 벗어나지 않으면
        return True
    return False
def check_left(nowr, nowc, nowd):
    nextd = change_rotation(nowd)
    nextr = nowr + dr[nextd]
    nextc = nowc + dc[nextd]
    if(isInMap(nextr,nextc) and visited[nextr][nextc]):
        return 1, nextr, nextc, nextd #옵션, 다음위치, 다음 방향을 return
    else:
        return 2, nowr, nowc, nextd
def check_back(nowr, nowc, nowd):
    backd = change_rotation(change_rotation(nowd))
    nextr = nowr+dr[backd]
    nextc = nowc+dc[backd]

    if(isInMap(nextr, nextc)):
        return True, backd
    else:
        return False, backd
def start_robot(nowr, nowc, nowd):
    check_num = 0 #현재 위치에서 로테이션 횟수를 체크해줌
    visited[nowr][nowc] = False
    clean_num = 1
    while(True):
        option, nextr, nextc, nextd = check_left(nowr, nowc, nowd)
        if(option == 1): # 왼쪽에 청소 가능해서 왼쪽 위치로 변경한 경우
            nowr = nextr
            nowc = nextc
            nowd = nextd
            check_num = 0
            visited[nowr][nowc] = False
            clean_num+=1
        elif(option == 2):
            nowd = nextd
            check_num += 1 #로테이션 횟수를 증가시켜줌
        if(check_num == 4):
            flag, backd = check_back(nowr, nowc, nowd)
            if(flag == True):
                nowr = nowr + dr[backd]
                nowc = nowc + dc[backd]
                check_num = 0
            else:
                break
    return clean_num


for i in range(N):
    map1.append(list(map(int, input().split())))
print(start_robot(r,c,d))

