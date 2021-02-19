dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def isin(y, x):
    if(0<=y<N and 0<=x<N):
        return True
    return False
def find_road(y, x):
    cnt = 1
    if(visited[y][x]!= -1):
        return visited[y][x]
    for i in range(4):
        nextx = x + dx[i]
        nexty = y + dy[i]
        if(isin(nexty, nextx)):
            if(forest[nexty][nextx]>forest[y][x]):
                cnt = max(cnt, find_road(nexty, nextx) + 1)

    visited[y][x] = cnt
    return cnt

if __name__ == "__main__":
    N = int(input())
    forest = []
    visited = [[-1]*N for _ in range(N)]
    for i in range(N):
        forest.append(list(map(int, input().split())))
    answer = 1
    for i in range(N):
        for j in range(N):
            answer = max(answer,find_road(i, j))
    print(answer)