dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
def isin(y, x):
    if 0<=y<N and 0<=x<N:
        return True
    return False
def find_block(y, x, visited, arr):
    queue = []
    queue.append([y, x])
    bnum = 1
    restore_list = []
    visited[y][x] = True
    check_num = arr[y][x]
    while(queue):
        ny, nx = queue.pop(0)
        for i in range(4):
            nexty, nextx = ny+dy[i], nx+dx[i]
            if(isin(nexty, nextx) and not visited[nexty][nextx]):
                if(arr[nexty][nextx] == check_num or arr[nexty][nextx] == 0):
                    if arr[nexty][nextx] == 0:
                        restore_list.append([nexty, nextx])
                    visited[nexty][nextx] = True
                    bnum+=1
                    queue.append([nexty, nextx])
    
    for i in restore_list:
        ny, nx = i
        visited[ny][nx] = False
    return [bnum, len(restore_list), y, x]
def delete_block(y, x, arr):
    visited = [[False]*N for _ in range(N)]
    visited[y][x] = True
    queue = []
    queue.append([y, x])
    check_num = arr[y][x]
    arr[y][x] = -2
    while(queue):
        y, x = queue.pop(0)
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if(isin(ny, nx) and not visited[ny][nx]):
                if(arr[ny][nx] == 0 or arr[ny][nx] == check_num):
                    arr[ny][nx] = -2
                    visited[ny][nx] = True
                    queue.append([ny, nx])
    return arr

def start(arr):
    score = 0
    while(True):
        candidate_list = []

        visited = [[False]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and arr[i][j]>0:
                    candidate_list.append(find_block(i, j, visited, arr))
        if len(candidate_list) == 0:
            break
        candidate_list.sort(key = lambda x:(-x[0], -x[1], -x[2], -x[3]))            
        b_size, s_b, y, x = candidate_list[0]
        if b_size<2:
            break
        score+=b_size**2
        arr = delete_block(y, x, arr)
        arr = down(arr)
        arr = rotate(arr)
        arr = down(arr)
    return score
def rotate(arr):
    temp = []
    for i in range(N-1, -1, -1):
        new_temp = []
        for j in range(N):
            new_temp.append(arr[j][i])
        temp.append(new_temp)
    return temp
def find_blank(arr):
    b_list = []
    for i in range(N):
        if arr[i] == -1:
            b_list.append(i)
    return b_list
def down(arr):

    for i in range(N):
        temp = []
        for j in range(N-1, -1, -1):
            temp.append(arr[j][i])
        
        b_list = find_blank(temp)
        b_list.append(N)

        starti = 0
        new_line = []
        for k in b_list:
            length = k - starti
            insert_num = 0
            for n in temp[starti:k]:
                if n>-1:
                    new_line.append(n)
                    insert_num+=1

            for n in range(length-insert_num):
                new_line.append(-2)
            if k != N:
                new_line.append(-1)
            starti = k+1
        index = 0
        for j in range(N-1, -1, -1):
            arr[j][i] = new_line[index]
            index+=1
    return arr



if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(start(board))