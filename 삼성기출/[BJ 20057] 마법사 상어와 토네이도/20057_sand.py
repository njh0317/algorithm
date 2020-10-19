arr = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
out_sand = 0

def isIn(x, y, N):
    if(0<=x<N and 0<=y<N):
        return True
    return False
def move_sand(N,x,y,ndir):

    global out_sand
    left = (ndir+1)%4
    right = (ndir+3)%4
    back = (ndir+2)%4
    front = ndir
    sand = arr[y][x]
    now_sand = sand


    # 5% (앞으로 2칸)
    move_sand = int(now_sand*0.05)
    nextx = x + dx[front]*2
    nexty = y + dy[front]*2

    if(isIn(nextx, nexty, N)):
        arr[nexty][nextx]+=move_sand
    else:
        out_sand+=move_sand
    sand-=move_sand

    # 10% (앞으로 1칸 오른쪽으로 1칸 혹은 앞으로 1칸 왼쪽으로 1칸)
    move_sand = int(now_sand*0.1)
    nextx = x + dx[front] + dx[right]
    nexty = y + dy[front] + dy[right]

    if(isIn(nextx, nexty, N)):
        arr[nexty][nextx]+=move_sand
    else:
        out_sand+=move_sand
    sand-=move_sand

    move_sand = int(now_sand*0.1)
    nextx = x + dx[front] + dx[left]
    nexty = y + dy[front] + dy[left]

    if(isIn(nextx, nexty, N)):
        arr[nexty][nextx]+=move_sand
    else:
        out_sand+=move_sand
    sand-=move_sand
    # 7% (오른쪽으로 1칸 혹은 왼쪽으로 1칸)
    move_sand = int(now_sand*0.07)
    nextx = x + dx[right]
    nexty = y + dy[right]

    if(isIn(nextx, nexty, N)):
        arr[nexty][nextx]+=move_sand
    else:
        out_sand+=move_sand
    sand-=move_sand

    move_sand = int(now_sand*0.07)
    nextx = x + dx[left]
    nexty = y + dy[left]

    if(isIn(nextx, nexty, N)):
        arr[nexty][nextx]+=move_sand
    else:
        out_sand+=move_sand
    sand-=move_sand

    # 2% (오른쪽으로 2칸 혹은 왼쪽으로 2칸)
    move_sand = int(now_sand*0.02)
    nextx = x + dx[right]*2
    nexty = y + dy[right]*2

    if(isIn(nextx, nexty, N)):
        arr[nexty][nextx]+=move_sand
    else:
        out_sand+=move_sand
    sand-=move_sand

    move_sand = int(now_sand*0.02)
    nextx = x + dx[left]*2
    nexty = y + dy[left]*2

    if(isIn(nextx, nexty, N)):
        arr[nexty][nextx]+=move_sand
    else:
        out_sand+=move_sand
    sand-=move_sand

    # 1% (뒤로 1칸 오른쪽으로 1칸 혹은 뒤로 1칸 왼쪽으로 1칸)
    move_sand = int(now_sand*0.01)
    nextx = x + dx[back] + dx[right]
    nexty = y + dy[back] + dy[right]

    if(isIn(nextx, nexty, N)):
        arr[nexty][nextx]+=move_sand
    else:
        out_sand+=move_sand
    sand-=move_sand

    move_sand = int(now_sand*0.01)
    nextx = x + dx[back] + dx[left]
    nexty = y + dy[back] + dy[left]

    if(isIn(nextx, nexty, N)):
        arr[nexty][nextx]+=move_sand
    else:
        out_sand+=move_sand
    sand-=move_sand

    #알파 앞으로 1칸
    move_sand = sand
    nextx = x + dx[front]
    nexty = y + dy[front]
    if(isIn(nextx, nexty, N)):
        arr[nexty][nextx]+=move_sand
    else:
        out_sand+=move_sand
    sand-=move_sand
    arr[y][x] = 0
    

def move_finger(N, x, y):
    start_num = 1
    ndir = 0
    flag = 0
    while(True):
        for i in range(2):
            for j in range(start_num):
                x = x + dx[ndir]
                y = y + dy[ndir]
                move_sand(N,x,y,ndir)
                if(x == 0 and y == 0):
                    flag = 1
                    break
            if(flag == 1):
                break
            ndir = (ndir+1)%4
        if(flag == 1):
            break
        start_num+=1



if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        arr.append(list(map(int, input().split())))
    move_finger(N, N//2, N//2)
    print(out_sand)

    
