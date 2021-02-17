INF = 99999999999
is_minus = False
def init():
    for i in range(N):
        bus[i+1] = {}
def bellman_ford(graph, start):
    distance = {}
    for node in graph:
        distance[node] = INF
    distance[start] = 0

    for i in range(N):
        for node in graph:
            for neighbor in graph[node]:
                if(distance[node]!=INF and distance[neighbor]>distance[node]+graph[node][neighbor]):
                    distance[neighbor] = distance[node]+graph[node][neighbor]
                    if(i == N-1):
                        global is_minus
                        is_minus = True

    return distance

if __name__ == "__main__":
    N, M = map(int, input().split())
    bus = {}
    init()
    for i in range(M):
        start, end, time = map(int, input().split())
        if(end in bus[start]):
            bus[start][end] = min(time, bus[start][end])
        else:
            bus[start][end] = time
    result = bellman_ford(bus, 1)
    if(is_minus):
        print(-1)
    else:
        for node, value in result.items():
            if(node!=1):
                if(value == INF):
                    print(-1)
                else:
                    print(value)
