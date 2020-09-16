
N,M = map(int, input().split())

ice = []
for i in range(N):
    ice.append(list(map(int,input())))

def dfs(x,y):
    #종료조건 : 범위를 벗어나는 경우
    if( x >= N or x <= -1 or y>=M or y<=-1):
        return False
    if(ice[x][y]==0):
        ice[x][y]=1
        dfs(x+1, y)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        #네 방향을 다 갔음에도 더이상 갈 곳이 없을 때 True로 종료
        return True

    return False
print(ice)
num=0
for i in range(0,N):
    for j in range(0,M):
        if(ice[i][j]==0):
            if(True == dfs(i,j)):
                print(ice)
                num=num+1


print(num)




