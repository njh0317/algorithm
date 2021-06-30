def init(n, edge):
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    for e1, e2 in edge:
        graph[e1].append(e2)
        graph[e2].append(e1)
    return graph

def bfs(n, graph):
    queue = []
    queue.append(1)
    visited = [-1 for _ in range(n+1)]
    visited[1] = 0
    max_num = 0
    while(queue):
        vertex = queue.pop(0)

        for e in graph[vertex]:
            if visited[e] == -1:
                visited[e] = visited[vertex]+1
                max_num = visited[e]
                queue.append(e)
    return visited.count(max_num)

    

def solution(n, edge):
    answer = 0
    graph = init(n, edge)
    answer = bfs(n, graph)
    return answer
if __name__ == "__main__":
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, vertex))