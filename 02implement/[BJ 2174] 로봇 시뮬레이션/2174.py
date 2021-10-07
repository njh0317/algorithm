dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
direct = {'N' : 0, 'E' : 1, 'S' : 2, 'W' : 3}

def isin(y, x, A, B): # 벽에 부딪힘
    if(0<=y<B and 0<=x<A):
        return True
    return False

if __name__ == "__main__":
    A, B = map(int, input().split())
    N, M = map(int, input().split())

    visited = [[0]*(A) for _ in range(B)]
    robot = {}

    for i in range(1, N+1):
        x, y, d = input().split()
        x, y = int(x)-1, B-int(y)
        robot[i] = [x, y, direct[d]]
        visited[y][x] = i
    
    flag = True
    for i in range(M):
        r, ctype, citer = input().split()
        r, citer = int(r), int(citer)
        if(ctype == 'F'):
            originrobot = robot[r] #x, y, direction
            x, y, d = originrobot
            for k in range(citer):
                nextx, nexty = x + dx[d], y + dy[d]
                if(not isin(nexty, nextx, A, B)):
                    flag = False
                    print("Robot "+str(r)+" crashes into the wall")
                    break
                if(visited[nexty][nextx] != 0):
                    print("Robot "+str(r)+" crashes into robot "+str(visited[nexty][nextx]))
                    flag = False
                    break
                x, y = nextx, nexty

            if(not flag):
                break
            visited[originrobot[1]][originrobot[0]] = 0
            visited[y][x] = r
            robot[r] = [x, y, d]
        elif(ctype == 'L'):
            citer %= 4
            origindirect = robot[r][2]
            origindirect = ((origindirect-citer)+4)%4
            robot[r][2] = origindirect
        else:
            citer %= 4
            origindirect = robot[r][2]
            origindirect = (origindirect+citer)%4
            robot[r][2] = origindirect

    if(flag):
        print("OK")