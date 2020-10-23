N, Q = map(int, input().split())
arr = []
level = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
check = [[True]*(2**N) for _ in range(2**N)]
big_ice = 0
def print_arr():
    for i in arr:
        print(i)
    print()
    
def isin(x, y):
    if(0<=x<2**N and 0<=y<2**N):
        return True
    return False
def count():
    sum_ice = 0

    for i in range(2**N):
        for j in range(2**N):
            sum_ice+=arr[i][j]
    return sum_ice
def melt():
    width = 2**N
    visited = [[False]*width for _ in range(width)]

    for i in range(width):
        for j in range(width):
            num=0
            if(arr[i][j]==0):
                continue
            for k in range(4):
                nextx = j+dx[k]
                nexty = i+dy[k]
                if(isin(nextx, nexty)):
                    if(arr[nexty][nextx]!=0):
                        num+=1

            if(num<3):
                visited[i][j] = True

    for i in range(width):
        for j in range(width):
            if(visited[i][j]):
                arr[i][j]-=1

def find_big_ice(y,x):
    global check
    global big_ice
    num = 0
    queue = []
    queue.append([x,y])
    check[y][x] = False
    while(queue):
        vertex = queue.pop(0)
        x = vertex[0]
        y = vertex[1]
        num+=1
        for i in range(4):
            nexty = y + dy[i]
            nextx = x + dx[i]
            if(isin(nextx, nexty)):
                if(check[nexty][nextx] and arr[nexty][nextx]>0):
                    check[nexty][nextx]=False
                    queue.append([nextx, nexty])
    big_ice = max(big_ice, num)
    return num

def rotate(level_n):
    nwidth = 2**N
    width = 2**level_n

    for i in range(0, nwidth, width):
        for j in range(0, nwidth, width):
            temp = []
            for k in range(i+width-1, i-1, -1):
                new_temp = []
                for l in range(j, j+width):
                    new_temp.append(arr[k][l])
                temp.append(new_temp)
            for k in range(j, j+width):
                for l in range(i, i+width):
                    arr[l][k] = temp[k-j][l-i]
    


if __name__ == "__main__":
    width = 2**N
    
    for i in range(width):
        arr.append(list(map(int, input().split())))
    
    level = list(map(int, input().split()))
    num = 1
    for i in range(Q):
        if(level[i]!=0):
            rotate(level[i])
        melt()   
    for i in range(width):
        for j in range(width):
            if(arr[i][j]>0 and check[i][j]):
                find_big_ice(i, j)
    print(count())
    print(big_ice)