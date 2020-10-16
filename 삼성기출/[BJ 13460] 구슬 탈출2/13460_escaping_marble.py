import copy
N, M =map(int, input().split())
arr = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def isIn(nowx, nowy):
    if(0>=nowy or nowy>=N-1 or 0>=nowx or nowx>=M-1 or arr[nowy][nowx] == '#'):
        return False
    return True
def change_loc(nowx, nowy, dir, char):
    arr[nowy][nowx] = '.'
    while(True):
        nextx = nowx+dx[dir]
        nexty = nowy+dy[dir]
        if(isIn(nextx, nexty) == False or arr[nexty][nextx] == 'R' or arr[nexty][nextx] == 'B'):
            arr[nowy][nowx] = char
            break
        nowx = nextx
        nowy = nexty
        if(arr[nowy][nowx] == 'O'):
            break
    return nowx, nowy

def check_loc(ax,ay, bx, by, dir):
    global arr
    temp_arr = copy.deepcopy(arr)
    if(dir == 0): #위쪽, 더 윗쪽에 위치한 것 먼저
        if(ay<=by):
            ax,ay = change_loc(ax,ay,dir,'R')
            bx,by = change_loc(bx,by,dir,'B')
        else:
            bx, by = change_loc(bx, by, dir, 'B')
            ax, ay = change_loc(ax, ay, dir, 'R')

    elif(dir == 1):
        if (ay >= by):
            ax, ay = change_loc(ax, ay, dir, 'R')
            bx, by = change_loc(bx, by, dir, 'B')
        else:
            bx, by = change_loc(bx, by, dir, 'B')
            ax, ay = change_loc(ax, ay, dir, 'R')

    elif(dir == 2):
        if (ax <= bx):
            ax, ay = change_loc(ax, ay, dir, 'R')
            bx, by = change_loc(bx, by, dir, 'B')
        else:
            bx, by = change_loc(bx, by, dir, 'B')
            ax, ay = change_loc(ax, ay, dir, 'R')
    elif(dir == 3):
        if (ax >= bx):
            ax, ay = change_loc(ax, ay, dir, 'R')
            bx, by = change_loc(bx, by, dir, 'B')
        else:
            bx, by = change_loc(bx, by, dir, 'B')
            ax, ay = change_loc(ax, ay, dir, 'R')
    arr = temp_arr
    return ax,ay, bx, by
def BFS(a_x, a_y, b_x, b_y):

    queue = []
    queue.append([a_x, a_y, b_x, b_y, 0])
    time = 0
    while(queue):
        vertex = queue.pop(0)
        ax = vertex[0]
        ay = vertex[1]
        bx = vertex[2]
        by = vertex[3]
        num = vertex[4]
        arr[ay][ax] = 'R'
        arr[by][bx] = 'B'
        if(num>=10):
            return -1
        for i in range(4):
            newax, neway, newbx, newby = check_loc(ax,ay,bx,by,i)
            if(newax == ax and neway == ay and newbx == bx and newby == by):
                continue
            if(arr[newby][newbx] == 'O'):
                continue
            if(arr[neway][newax] == 'O'):
                return num+1
            queue.append([newax,neway,newbx,newby,num+1])
        time+=1
        arr[ay][ax] = '.'
        arr[by][bx] = '.'
    return -1
if __name__ == "__main__":
    for i in range(N):
        newarr = list(input())
        arr.append(newarr)
        if('R'in newarr):
            r_x = newarr.index('R')
            r_y = i
        if('B' in newarr):
            b_x = newarr.index('B')
            b_y = i

    print(BFS(r_x, r_y, b_x, b_y))