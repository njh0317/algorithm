# 32 분 
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def isin(y, x):
    if(0<=y<N and 0<=x<N):
        return True
    return False

def eatFish(babyshark, arr):
    babyshark_size = 2
    eatnum = 0
    t = 0


    while(True):
        #먹을 수 있는 물고기 위치 찾기
        visited = [[-1]*N for _ in range(N)]
        y, x = babyshark
        visited[y][x] = 0
        queue = [[y, x]]

        will_eat_fish = []
        will_eat_fish_move_num = -1 #먹을 물고기를 찾았는지 여부 , 이동 거리 저장
        endFlag = False
        while(queue):
            y, x = queue.pop(0)
            move_num = visited[y][x]

            for i in range(4):
                nexty, nextx = y + dy[i], x + dx[i]
                if(isin(nexty, nextx) and visited[nexty][nextx] == -1 and arr[nexty][nextx]<=babyshark_size):
                    #이동 가능한 위치
                    visited[nexty][nextx] = move_num+1
                    if(0 < arr[nexty][nextx]<babyshark_size): #먹을 수 있는 물고기 발견
                        if(will_eat_fish_move_num == -1):
                            will_eat_fish_move_num = visited[nexty][nextx]
                            will_eat_fish.append([nexty, nextx])
                        else:
                            if(will_eat_fish_move_num == visited[nexty][nextx]):
                                will_eat_fish.append([nexty, nextx])
                            else:
                                endFlag = True
                                break
                    queue.append([nexty, nextx])
                if(endFlag): break
            if(endFlag): break


        #물고기를 먹을 수 없으면 break
        if(will_eat_fish_move_num == -1):
            break
        #물고기를 먹을 수 있으면, 시간 올리고 물고기 먹고 이동
        t+=will_eat_fish_move_num
        will_eat_fish.sort(key = lambda x:(x[0], x[1]))
        eatnum+=1
        y, x = babyshark
        eatfish_y, eatfish_x = will_eat_fish[0]
        arr[eatfish_y][eatfish_x] = 9
        arr[y][x] = 0
        babyshark = [eatfish_y, eatfish_x]

        if(eatnum == babyshark_size): 
            eatnum = 0
            babyshark_size+=1
    
    return t

if __name__ == "__main__":
    N = int(input())
    babyshark = [-1, -1] #y, x
    arr = []
    for i in range(N):
        newarr = list(map(int, input().split()))
        arr.append(newarr)
        if(babyshark[0] == -1):
            for j in range(N):
                if(newarr[j] == 9):
                    babyshark = [i, j]
                    break
    

    print(eatFish(babyshark, arr))