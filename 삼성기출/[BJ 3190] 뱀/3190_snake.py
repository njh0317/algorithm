N = int(input())
K = int(input())
apple = []
for i in range(K):
    apple.append(list(map(int, input().split())))
snake = [[1,1]]

dx = [0, 1, 0, -1]#열
dy = [-1, 0, 1, 0]#행

now_dir = 1
x = 1
y = 1
rotation = int(input())
dir_change_info = []
for i in range(rotation):
    dir_change_info.append(list(input().split()))

time = 0
flag = True
while(True):

    time+=1
    x = x + dx[now_dir]
    y = y + dy[now_dir]
    if(x==0 or y == 0 or x == N+1 or y == N+1):
        flag = False
        break
    if([y,x] in snake):
        flag = False
        break
    snake.append([y,x])
    if([y,x] in apple):
        apple.remove([y,x])
    else:
        del snake[0]
    if(len(dir_change_info)>0):
        if(int(dir_change_info[0][0])==time):
            if(str(dir_change_info[0][1])=='D'):
                now_dir = (now_dir+1)%4
            else:
                now_dir = (now_dir-1) if( now_dir -1 != -1) else 3
            del dir_change_info[0]
        
print(time)


            


