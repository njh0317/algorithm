import copy
N, M = map(int, input().split())
arr = []
cctv_num = 0
dc = [-1,0,1,0]
dr = [0,1,0,-1]
min_num = 9999
def CCTV_info(num):
    if(num==1):
        return [[0],[1],[2],[3]]
    elif(num==2):
        return [[1,3],[0,2]]
    elif(num==3):
        return [[0,1],[1,2],[2,3],[3,0]]
    elif(num==4):
        return [[0,1,2],[0,1,3],[0,2,3],[1,2,3]]
    elif(num==5):
        return [[0,1,2,3]]
def isInarr(nowc,nowr):
    if(0<=nowc<N and 0<=nowr<M):
        if(arr[nowc][nowr]!=6):#벽이 아니면
            return True
    return False
def DFS(nownum, cctv_list, choose_list): ## DFS 하면서 전체 탐색

    if(nownum == cctv_num):
        #print(cctv_list,choose_list)
        checkarr(cctv_list, choose_list)
        return

    dir_list = CCTV_info(cctv_list[nownum][2])
    for i in range(len(dir_list)):
        choose_list.append(dir_list[i])
        DFS(nownum+1, cctv_list, choose_list)
        choose_list.pop(-1)
def checkarr(cctv_list, choose_list):
    global arr
    global min_num
    temp = copy.deepcopy(arr)
    for i in range(cctv_num):
        startc = cctv_list[i][0]
        startr = cctv_list[i][1]

        choose_dir = choose_list[i]
        for j in choose_dir:
            nowc = startc
            nowr = startr
            while(True):
                nextc = nowc + dc[j]
                nextr = nowr + dr[j]
                if(isInarr(nextc, nextr)): #벽이 아니고 영역을 벗어나지 않으면
                    nowc = nextc
                    nowr = nextr
                    if(arr[nextc][nextr]!=0):#CCTV 이거나 이미 영역 표시가 완료되었으면 (-1) 이면
                        continue #그냥 통과
                    else: #0이면
                        arr[nextc][nextr] = -1 #cctv 가 감시중임을 표시

                else:
                    break
    check = 0
    for i in range(N):
        for j in range(M):
            if(arr[i][j]==0):
                check+=1
    min_num = min(min_num, check)
    arr= temp
    return

cctv_list = []
for i in range(N):
    new_arr = list(map(int, input().split()))
    for j in range(M):
        if(new_arr[j]!=0 and new_arr[j]!=6):
            cctv_num+=1
            cctv_list.append([i,j,new_arr[j]])
    arr.append(new_arr)

DFS(0, cctv_list, [])
print(min_num)
