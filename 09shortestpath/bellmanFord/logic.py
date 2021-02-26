def bellman_ford(graph, start):
    #거리값, 각 정점의 이전 정점을 저장할 딕셔너리 
    distance, predecessor = dict(), dict()
   
    #거리 값을 모두 무한대로 초기화/ 이전 정점은 None으로 초기화
    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[start] = 0

    #간선 개수(V-1)만큼 반복
    for _ in range(len(graph)-1):
        for node in graph:
            #각 정점마다 모든 인접 정점들을 탐색 
            for neighbor in graph[node]:
                #[기존 인접 정점까지의 거리 > 기존 현재 정점까지 거리 + 현재 정점부터 인접 정점까지 거리]인 경우 갱신
                if distance[node]!= float('inf') and distance[neighbor]>distance[node]+graph[node][neighbor]:
                    distance[neighbor] = distance[node] + graph[node][neighbor]
                    predecessor[neighbor] = node
    #음수 사이클 존재 여부 검사 : V-1 번 반복 이후에도 갱신할 거리 값이 존재한다면 음수 사이클 존재
    for node in graph:
        for neighbor in graph[node]:
            if(distance[neighbor] > distance[node] + graph[node][neighbor]):
                return -1, "음수 사이클 존재"
    return distance, predecessor
if __name__ == "__main__":
    #음수 사이클이 존재하지 않는 경우 
    # graph = {
    #     'A': {'B': -1, 'C':  4},
    #     'B': {'C':  3, 'D':  2, 'E':  2},
    #     'C': {},
    #     'D': {'B':  1, 'C':  5},
    #     'E': {'D': -3}
    # }

    #음수 사이클이 존재하는 예시 
    graph = {
        'A': {'B': -1, 'C':  4},
        'B': {'C':  3, 'D':  2, 'E':  2},
        'C': {'A': -5},
        'D': {'B':  1, 'C':  5},
        'E': {'D': -3}
    }   
    distance, predecessor = bellman_ford(graph, start='A')
    print(distance)
    print(predecessor)
