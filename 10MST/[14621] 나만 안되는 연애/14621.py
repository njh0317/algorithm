import heapq
from collections import defaultdict
visited = {}
distances = {}
graph = defaultdict(list)

def make_set(v):
    visited[v] = False
    distances[v] = float('inf')

def prim(start, school_info):
    queue = []
    visited[start] = True
    distances[start] = 0
    mst = []
    total_weight = 0
    for edge in graph[start]:
        weight, x1, x2 = edge
        if(school_info[x1-1]!= school_info[x2-1]):
            heapq.heappush(queue, edge)
    
    while(queue):
        weight, x1, x2 = heapq.heappop(queue)
        if(visited[x2] == False):
            visited[x2] = True
            distances[x2] = weight
            mst.append((weight, x1, x2))
            total_weight+=weight
            for edge in graph[x2]:
                weight, x1, x2 = edge
                if(school_info[x1-1]!= school_info[x2-1]):
                    heapq.heappush(queue, edge)
    return mst, total_weight
if __name__ == "__main__":
    N, M = map(int, input().split())
    school_info = list(input().split())
    for i in range(N):
        make_set(i+1)
    for i in range(M):
        u, v, d = map(int, input().split())
        graph[u].append((d, u, v))
        graph[v].append((d, v, u))

    answer, total_weight = prim(1, school_info)
    if(len(answer)!=N-1):
        print(-1)
    else:
        print(total_weight)

    

