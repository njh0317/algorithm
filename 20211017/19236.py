#1시간
import copy
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

total_eat = 0
def isin(y, x):
    if(0<=y<4 and 0<=x<4):
        return True
    return False

def move_fish(arr, fish):
    # 물고기 이동 ( 번호가 작은 물고기 부터 순서대로 이동, 물고기는 한칸 이동, 
    #   이동 가능한 칸 : 빈칸, 다른 물고기가 있는 칸) - 이동할 수 있을 때 까지 방향을 45도 반시계 회전 
    #   서로의 위치를 바꾸는 방식으로 이동
    newarr = copy.deepcopy(arr)
    newfish = copy.deepcopy(fish)

    for i in range(1, 17):
        if(i in newfish.keys()):
            y, x, d = newfish[i]
            for j in range(8):
                nextd = (d+j)%8
                nexty, nextx = y + dy[nextd], x + dx[nextd]
                if(isin(nexty, nextx) and newarr[nexty][nextx] != -1):
                    if(newarr[nexty][nextx] == 0):
                        newarr[nexty][nextx], newarr[y][x] = i, 0 
                        newfish[i] = [nexty, nextx, nextd]
                    else:
                        change_fish = newarr[nexty][nextx]
                        newarr[nexty][nextx], newarr[y][x] = i, change_fish 

                        newfish[i] = [nexty, nextx, nextd]
                        newfish[change_fish][0], newfish[change_fish][1] = y, x
                    break
    return newarr, newfish

def backtracking(arr, fish, shark, eat):
    i = 1
    newarr, newfish = move_fish(arr, fish)
    sharky, sharkx, sharkd = shark
    newarr[sharky][sharkx] = 0


    while(True):
        nexty, nextx = sharky+dy[sharkd]*i, sharkx+dx[sharkd]*i
        if(isin(nexty, nextx)):
            if(newarr[nexty][nextx]!=0):
                # 물고기 먹기 (이동)
                eatfish_num = newarr[nexty][nextx]
                eatfish_info = newfish[eatfish_num]
                newarr[nexty][nextx] = -1
                del newfish[eatfish_num]
                
                # 물고기 이동
                
                #backtracking 호출
                backtracking(newarr, newfish, [nexty, nextx, eatfish_info[2]], eat+eatfish_num)
                # 물고기 원위치
                newarr[nexty][nextx] = eatfish_num
                newfish[eatfish_num] = eatfish_info
            
            i+=1
        else:
            break
    newarr[sharky][sharkx] = -1
    global total_eat
    total_eat = max(total_eat, eat)
    return

if __name__ == "__main__":
    arr = [[-1]*4 for _ in range(4)]
    fish = {}
    for i in range(4):
        new_fish_info = list(map(int, input().split()))

        for j in range(4):
            a, b = new_fish_info[j*2],new_fish_info[j*2+1]
            arr[i][j] = a
            fish[a] = [i, j, b-1]
    
    total_eat = arr[0][0]
    shark = [0, 0, fish[total_eat][2]]
    arr[0][0] = -1 #-1이 상어 위치
    del fish[total_eat]


    backtracking(arr, fish, shark, total_eat)
    print(total_eat)