# 4 2 0 0 8
# 0 2
# 3 4
# 5 6
# 7 8
# 4 4 4 1 3 3 3 2

N, M, x, y, K = map(int, input().split()) #세로 가로
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
command = list(map(int, input().split()))
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
def isIn(nowx, nowy):
    if(0<=nowx<N and 0<=nowy<M):
        return True
    return False
def change_dice(dice, dir):
    new_dice = [0]*7
    if(dir == 1):#동, 서, 북, 남
        new_dice[1] = dice[4]
        new_dice[2] = dice[2]
        new_dice[3] = dice[1]
        new_dice[4] = dice[6]
        new_dice[5] = dice[5]
        new_dice[6] = dice[3]
    elif(dir == 2):
        new_dice[1] = dice[3]
        new_dice[2] = dice[2]
        new_dice[3] = dice[6]
        new_dice[4] = dice[1]
        new_dice[5] = dice[5]
        new_dice[6] = dice[4]
    elif(dir == 3):
        new_dice[1] = dice[5]
        new_dice[2] = dice[1]
        new_dice[3] = dice[3]
        new_dice[4] = dice[4]
        new_dice[5] = dice[6]
        new_dice[6] = dice[2]
    elif(dir == 4):
        new_dice[1] = dice[2]
        new_dice[2] = dice[6]
        new_dice[3] = dice[3]
        new_dice[4] = dice[4]
        new_dice[5] = dice[1]
        new_dice[6] = dice[5]

    return new_dice

def start_dice():
    nowx, nowy = x, y
    dice = [0]*7
    for i in range(K):
        now_command = command[i]
        nextx = dx[now_command] + nowx
        nexty = dy[now_command] + nowy

        if(isIn(nextx, nexty) == False):
            continue
        dice = change_dice(dice, now_command)
        if(arr[nextx][nexty] == 0):
            arr[nextx][nexty] = dice[6]
        else:
            dice[6] = arr[nextx][nexty]
            arr[nextx][nexty] = 0
        nowx = nextx
        nowy = nexty
        print(dice[1])

start_dice()



