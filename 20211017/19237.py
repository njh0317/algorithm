dx = {1: 0, 2: 0, 3: -1, 4: 1}
dy = {1: -1, 2: 1, 3: 0, 4: 0}

shark_priority = {}
shark_position = {}
def getPriority(shark_num, now_direction):
    return shark_priority[shark_num][now_direction]
def isin(y, x, N):
    if (0<=y<N and 0<=x<N):
        return True
    return False
def moveShark(arr, N):
    smell_position = [[[-1, -1]] * N for _ in range(N)]
    for t in range(1, 1001):
        # 냄새 뿌리기
        for i in range(N):
            for j in range(N):
                if(arr[i][j] != 0):
                    smell_position[i][j] = [k, arr[i][j]] #시간, 상어 번호
                    arr[i][j] = 0
        del_shark_list = []
        # 상어 이동
        for shark_num, shark_state in shark_position.items():
            #shark_state : y, x, 보고있는 방향

            # 1) 4방향 중 빈 곳이 있으면 그 곳으로 이동 (우선순위 기준 )
            priority = getPriority(shark_num, shark_state[2])
            change_shark_position = [-1, -1, -1]
            for p in priority:
                nexty, nextx = shark_state[0]+dy[p], shark_state[1]+dx[p]
                if(isin(nexty, nextx, N) and smell_position[nexty][nextx] == [-1, -1]):
                    change_shark_position = [nexty, nextx, p]
                    break
            
            if(change_shark_position == [-1, -1, -1]): # 빈 공간이 없어서 아직 못찾음 
                for p in priority:
                    nexty, nextx = shark_state[0]+dy[p], shark_state[1]+dx[p]
                    if(isin(nexty, nextx, N) and smell_position[nexty][nextx][1] == shark_num):
                        change_shark_position = [nexty, nextx, p]
                        break
            
            nexty, nextx, nextd = change_shark_position
            if(arr[nexty][nextx] == 0):
                arr[nexty][nextx] = shark_num
            else:
                if(shark_num<arr[nexty][nextx]):
                    del_shark_list.append(arr[nexty][nextx])
                    arr[nexty][nextx] = shark_num
                else:
                    del_shark_list.append(shark_num)
            shark_position[shark_num] = [nexty, nextx, nextd]
        for shark_num in del_shark_list:
            del shark_position[shark_num]

        # 냄새 하나씩 줄이기
        for i in range(N):
            for j in range(N):
                smell_time, smell_type = smell_position[i][j]
                if(smell_type != -1):
                    smell_time -= 1
                    if(smell_time == 0):
                        smell_position[i][j] = [-1, -1]
                    else:
                        smell_position[i][j] = [smell_time, smell_type]

        if len(shark_position) == 1: 
            return t
    return -1
if __name__ == "__main__":
    N, M, k = map(int, input().split())
    arr = []

    for i in range(N):
        newarr = list(map(int, input().split()))
        for j in range(N):
            if(newarr[j] != 0):
                shark_position[newarr[j]] = [i, j, 0]
    
        arr.append(newarr)

    start_direction = list(map(int, input().split()))

    for i in range(M):
        #i+1
        shark_num = i+1
        shark_position[shark_num][2] = start_direction[i]
        shark_priority[shark_num] = {}
        for j in range(4):
            shark_priority[shark_num][j+1] = list(map(int, input().split()))

    print(moveShark(arr, N))