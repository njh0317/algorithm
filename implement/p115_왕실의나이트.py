chess = ['a','b','c','d','e','f','g','h']
dx = [-2,-2,2,2,-1,-1,1,1]
dy = [-1,1,-1,1,-2,2,-2,2]

now_point = input()

now_x = chess.index(now_point[0])
now_y = int(now_point[1])-1


num=0

for i in range(8):
    nextX = now_x+dx[i]
    nextY = now_y+dy[i]
    if not(nextX<0 or nextY<0 or nextX>=8 or nextY>=8):
        num+=1
print(num)