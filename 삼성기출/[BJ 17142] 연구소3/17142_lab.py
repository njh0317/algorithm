# 7 3
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 2 0 1 1
# 0 1 0 0 0 0 0
# 2 1 0 0 0 0 2
from itertools import combinations
N, M = map(int, input().split())
arr = []
virus = []
min_time = 9999
dx = [0,0,-1,1] #상하좌우
dy = [-1,1,0,0]

def isIn(nowx, nowy):
    if(0<=nowx<N and 0<=nowy<N and arr[nowy][nowx]!=1):
        return True
    return False
def active_virus(num_list, zero_num):
    global min_time
    visited = [[0]*N for _ in range(N)]
    queue = []
    for i in num_list:
        queue.append([virus[i][0],virus[i][1], 0]) #x, y, time
        visited[virus[i][1]][virus[i][0]] = 0

    max_time = 0
    while(queue):
        vertex = queue.pop(0)
        x = vertex[0]
        y = vertex[1]
        time = vertex[2]
        if([x,y] not in virus):
            max_time = max(max_time, time)
        if (arr[y][x] != 2):
            zero_num -= 1
        if(zero_num == 0):
            break
        for i in range(4):
            nextx = x+dx[i]
            nexty = y+dy[i]
            if(isIn(nextx, nexty) and visited[nexty][nextx] == 0):
                visited[nexty][nextx] = 1
                queue.append([nextx, nexty, time+1])


    #if(check(visited) == True):
    if(zero_num == 0):
        min_time = min(min_time, max_time)

def make_comb(num, prev, num_list):
    if(num==M):
        #바이러스 활성화 함수 호출

        active_virus(num_list)
        return
    for i in range(prev, len(virus)):
        num_list.append(i)
        make_comb(num+1, i+1, num_list)
        num_list.pop(-1)


if __name__ == "__main__":
    zero_num = 0
    num_arr = []
    num = 0
    for i in range(N):
        new_arr = list(map(int, input().split()))
        for j in range(N):
            if(new_arr[j]==2):
                num_arr.append(num)
                num+=1
                virus.append([j, i])# 바이러스 위치 저장
            elif(new_arr[j] == 0):
                zero_num+=1
        arr.append(new_arr)
    #make_comb(0, 0, [])

    comb_list = list(combinations(num_arr, M))
    for i in comb_list:
        active_virus(list(i), zero_num)


    if(min_time == 9999):
        print(-1)
    else:
        print(min_time)