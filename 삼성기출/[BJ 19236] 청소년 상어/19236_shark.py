import copy
fish = []
di = [0, -1,-1,0,1,1,1,0,-1]
dj = [0,0,-1,-1,-1,0,1,1,1]
max_eat = 0
def change_dir(num):
    num +=1
    if(num == 9):
        num = 1
    return num
def change_fish_position(arr):
    #해당 번호가 없거나, 더이상 갈수 없으면 그냥 종료
    #해당 번호가 있고, 이동할 수 있으면 이동하고 종료
    fish_num = 1

    while(fish_num < 17):
        flag = False
        for i in range(4):
            for j in range(4):
                if(arr[i][j][0] == fish_num):
                    start_dir = arr[i][j][1]#시작 방향을 저장해줌
                    while(True):
                        nexti = i+di[arr[i][j][1]]
                        nextj = j+dj[arr[i][j][1]]
                        if(nexti !=-1 and nextj != -1 and nexti != 4 and nextj != 4):
                            if(arr[nexti][nextj][0]!= 0):
                            #경계를 넘지 않고, 위치에 상어가 존재하지 않으면
                            #두 물고기의 위치를 변경해준다.
                                temp = arr[nexti][nextj]
                                arr[nexti][nextj] = arr[i][j]
                                arr[i][j] = temp
                                break
                        arr[i][j][1] = change_dir(arr[i][j][1])
                        if(start_dir == arr[i][j][1]): #다시 원위치로 돌아오면 종료
                            break
                    flag = True
                    break
                if(flag == True):
                    break
            if(flag == True):
                break
        fish_num+=1
    return arr

def make_eat_list(arr, ni, nj, ndir):
    eat_list = []

    while(True):
        nexti = ni+di[ndir]
        nextj = nj+dj[ndir]
        if(nexti != -1 and nextj != -1 and nexti != 4 and nextj != 4):
            if(arr[nexti][nextj][0] != -1):
                eat_list.append([nexti, nextj])
            ni = nexti
            nj = nextj
        else:
            break
    return eat_list

def backtracking(arr, ni, nj, ndir, eat):
    global max_eat
    # print("before change")
    # for i in range(len(arr)):
    #     for j in range(len(arr[i])):
    #         print(arr[i][j][0], end=" ")
    #     print()
    # print()
    change_fish_position(arr)
    # print("after change")
    # for i in range(len(arr)):
    #     for j in range(len(arr[i])):
    #         print(arr[i][j][0], end=" ")
    #     print()
    # print()

    eat_list = make_eat_list(arr, ni, nj, ndir)
    if(len(eat_list) == 0):#먹을 수 있는 물고기가 없으면
        max_eat = max(max_eat, eat)
        return
    for i in eat_list:
        nexti = i[0]
        nextj = i[1]
        temp = copy.deepcopy(arr)
        now_eat = eat + arr[nexti][nextj][0]
        arr[ni][nj] = [-1,-1]
        arr[nexti][nextj] = [0, arr[nexti][nextj][1]]
        backtracking(arr, nexti, nextj, arr[nexti][nextj][1], now_eat)
        arr= temp
    return

for i in range(4):
    new_fish = []
    insert_fish = list(map(int, input().split()))
    for j in range(0, 8, 2):
        new_fish.append([insert_fish[j], insert_fish[j+1]])
    fish.append(new_fish)
eat = fish[0][0][0]
shark_dir = fish[0][0][1]
fish[0][0][0] = 0
backtracking(fish, 0, 0, shark_dir, eat)
print(max_eat)
