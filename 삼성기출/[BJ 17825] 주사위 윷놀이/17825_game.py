arr = list(map(int,input().split()))


max_score = 0
def backtracking(now, score, position):
    global max_score
    if(now == 10):
        max_score = max(max_score, score)
        return

    for i in range(4):
        if(position[i][0]!=-1):
            flag2 = True
            temp = position[i]
            nextposition, flag = horse_next_move(position[i][0], position[i][1], arr[now])
            for j in range(4):
                if(i!=j and position[j][0]!=-1):
                    if(position[j][0]== nextposition):
                        flag2 = False
                        break
            if(flag2 == False):
                continue
            if(nextposition!=-1):
                score+=nextposition
            position[i] = [nextposition, flag]
            backtracking(now+1, score, position)
            if(nextposition!=-1):
                score-=position[i][0]
            position[i] = temp



def horse_next_move(now_position, flag, dice_num):
    move_list = []
    next_position = 0
    if(10<= now_position < 20 and flag == 1):
        if(dice_num*3+now_position<20):
            next_position = dice_num*3+now_position
        else:
            dice_num -= ((19 - now_position) // 3 + 1)
            now_position = 25
            next_position = dice_num*5+now_position
        if(next_position == 30):
            flag = 2
        else:
            flag = 1
    elif(20<= now_position<25 and flag == 1):
        if(dice_num*2+now_position<25):
            next_position = dice_num*2+now_position
        else:
            now_position=25
            dice_num -= ((24-now_position)//2+1)
            next_position = dice_num*5+now_position
        if(next_position == 30):
            flag = 2
        else:
            flag = 1
    elif(((25 == now_position or 30<now_position<= 40) and flag == 1) or (flag == 2 and now_position==30)):
        next_position = dice_num*5+now_position
        if(next_position!=30):
            flag = 1
        else:
            flag = 2
    elif(25 < now_position  <=30 and flag ==1):
        now_position = 28
        dice_num-=1
        if(now_position - dice_num >= 25):
            next_position = now_position-dice_num
        else:
            dice_num-=(now_position-25)
            now_position = 25
            next_position = dice_num*5+now_position
        if(next_position == 30):
            flag = 2
    else:
        next_position = now_position+dice_num*2
        if(next_position == 10 or next_position == 20 or next_position == 30 or next_position == 40):
            flag = 1
        else:
            flag = 0
    if(next_position > 40):
        return -1, 0
    else:
        return next_position, flag

backtracking(0, 0, [[0,0],[0,0],[0,0],[0,0]])
print(max_score)

