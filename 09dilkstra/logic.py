import heapq

def dijkstra(graph, start):
    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start],start])

    while(queue):
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node]<current_distance:
            continue # 현재 거리보다 이미 작으면 계산할 필요가 없음
        for adjacent, weight in graph[current_node].items():
            distance = current_distance+weight
            if distance < distances[adjacent]:
                #계산한 거리가 기존 거리보다 작으면
                #업데이트
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
    return distances


mygraph = {
    'A':{'B':8, 'C':1, 'D':2},
    'B':{},
    'C':{'B':5, 'D':2},
    'D':{'E':3, 'F':5},
    'E':{'F':1},
    'F':{'A':5}

}
print(dijkstra(mygraph, 'A'))