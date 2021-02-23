dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
max_flower = 0
def isin(x, y):
    if(0<=x<M and 0<=y<N):
        return True
    return False
def start_time():
    queue = []
    visited2 = [[[-1, 'N']]*M for _ in range(N)]
    flower = 0
    for i in range(N):
        for j in range(M):
            if(visited[i][j]!='N'):
                queue.append([i, j, visited[i][j], 0]) #y, x, G or R, time
                visited2[i][j] = [0, visited[i][j]]
    while(queue):
        nowy, nowx, color, time = queue.pop(0)
        if(visited2[nowy][nowx][1] == 'F'):
            continue
        for i in range(4):
            nexty = nowy + dy[i]
            nextx = nowx + dx[i]
            if(isin(nextx, nexty)):
                is_possible, color2 = visited2[nexty][nextx]
                if(garden[nexty][nextx]!=0):
                    if(is_possible == -1):
                        visited2[nexty][nextx] = [time+1, color]
                        queue.append([nexty, nextx, color, time+1])
                    elif(is_possible == time+1 and color2 != color):
                        visited2[nexty][nextx] = [9999, 'F']
                        flower+=1
    global max_flower
    max_flower = max(max_flower, flower)
    return
def setculture(leftG, leftR, index):
    if(leftG == 0 and leftR == 0):
        start_time()
        return 
    for i in range(index, len(possible_garden)):
        y, x = possible_garden[i]
        if(visited[y][x] == 'N'):
            if(leftG!=0):
                visited[y][x] = 'G'
                setculture(leftG-1, leftR, i+1)
            if(leftR!=0):
                visited[y][x] = 'R'
                setculture(leftG, leftR-1, i+1)
            visited[y][x] = 'N'

    


if __name__ == "__main__":
    N, M, G, R = map(int, input().split())
    garden = []
    possible_garden = []
    visited = [['N']*M for _ in range(N)]
    for i in range(N):
        new_garden = list(map(int, input().split()))
        garden.append(new_garden)
        for j in range(M):
            if(new_garden[j] == 2):
                possible_garden.append([i, j])

    setculture(G, R, 0)
    print(max_flower)