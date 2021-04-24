import heapq
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def isin(y, x):
    if(0<=y<n and 0<=x<n):
        return True
    return False
def dilkstra():
    distances = [[float('inf')]*n for _ in range(n)]
    distances[0][0] = 0
    queue = [[0, 0, 0]]
    while(queue):
        weight, y, x = heapq.heappop(queue)
        # if(y == n-1 and x == n-1):
        #     break
        if distances[y][x]<weight:
            continue
        for i in range(4):
            nexty, nextx = y+dy[i], x+dx[i]
            if(isin(nexty, nextx)):
                if arr[nexty][nextx] == '1':
                    next_weight = 0
                else:
                    next_weight = 1
                next_distance = weight+next_weight
                if(next_distance<distances[nexty][nextx]):
                    distances[nexty][nextx] = next_distance
                    heapq.heappush(queue, [next_distance, nexty, nextx])
    return distances

if __name__ == "__main__":
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append(list(input()))
    print(dilkstra()[n-1][n-1])
