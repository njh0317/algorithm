import heapq

def dijkstra(graph, start):
    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while(queue):
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue
        for adjacent, weight in graph[current_node].items():
            now_weight = current_distance + weight
            if(now_weight<distances[adjacent]):
                distances[adjacent] = now_weight
                heapq.heappush(queue, [now_weight, adjacent])

    return distances

V, E = map(int, input().split())
K = int(input())

mygraph = {}
for i in range(V):
    mygraph[i+1] = {}

for i in range(E):
    u, v, w = map(int, input().split())
    if(v in mygraph[u].keys()):
        mygraph[u][v] = min(mygraph[u][v], w)
    else:
        mygraph[u][v] = w
result = dijkstra(mygraph, K)

for i in result.items():
    if(i[1] == float('inf')):
        print("INF")
    else:
        print(i[1])
