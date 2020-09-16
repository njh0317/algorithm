from collections import deque
def bfs(graph, start, visited):
    #처음에 큐 하나 선언
    queue = deque([start])
    visited[start] = True

    while(queue):
        v=queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                #이미 큐에 추가된 점은 더이상 추가 되지 않아도 됨으로 방문했다고 표시해줌
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

bfs(graph,1,visited)#그래프, 시작점, 방문여부 저장공간