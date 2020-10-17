import sys
plus_nutrient = []
now_nutrient = []
dy = [-1,-1,-1,0,1,1,1,0]
dx = [-1,0,1,1,1,0,-1,-1]
def isIn(nowx, nowy, N):
    if(0<=nowx<N and 0<=nowy<N):
        return True
    return False
def spring(tree):
    trash_tree = []
    for i in tree[:]:
        x = i[0]
        y = i[1]
        age = i[2]

        if(now_nutrient[y][x]<age):
            trash_tree.append([x,y,age])
            tree.pop(tree.index([x,y,age]))
        else:
            now_nutrient[y][x]-=age ## 먹은 영양분 제거
            i[2]+=1 ## 한살 증가
    return tree, trash_tree
def summer(trash_tree):

    for i in trash_tree:
        now_nutrient[i[1]][i[0]]+=(i[2]//2)


def fall(tree, N):
    temp_tree = []

    for i in tree:
        if(i[2] % 5 == 0):
            for j in range(8):
                nextx = i[0]+dx[j]
                nexty = i[1]+dy[j]
                if(isIn(nextx,nexty, N)):
                    temp_tree.append([nextx, nexty, 1])

    return tree+temp_tree
def winter(N):
    for i in range(N):
        for j in range(N):
            now_nutrient[i][j] += plus_nutrient[j][i]

if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split()) #N*N 크기, M 나무 개수, K 시간
    tree = []
    now_nutrient = [[5]*N for _ in range(N)]
    for i in range(N):
        plus_nutrient.append(list(map(int, sys.stdin.readline().split())))

    for i in range(M):
        new_tree = list(map(int, sys.stdin.readline().split()))
        tree.append([new_tree[0]-1, new_tree[1]-1, new_tree[2]])

    for i in range(K):
        tree.sort(key=lambda x: x[2])
        tree, trash_tree = spring(tree)
        summer(trash_tree)
        tree = fall(tree,N)
        winter(N)
        if(len(tree) == 0):
            break
    print(len(tree))
