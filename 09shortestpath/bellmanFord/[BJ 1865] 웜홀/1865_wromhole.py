
INF = int(1e9)
def bellman_ford(start):
    distance = {}
    for i in range(1, N+1):
        distance[i] = INF
    distance[start] = 0

    for i in range(N):
        for edge in graph:
            start_node = edge[0]
            next_node = edge[1]
            cost = edge[2]
            if(distance[next_node]>distance[start_node]+cost):
                distance[next_node]=distance[start_node]+cost
                if(i == N-1):
                    return True

    return False

if __name__ == "__main__":
    TC = int(input())

    for t in range(TC):
        graph = []
        N, M, W = map(int, input().split())
        for m in range(M):
            S, E, T = map(int, input().split())
            graph.append([S, E, T])
            graph.append([E, S, T])
        for w in range(W):
            S, E, T = map(int, input().split())
            graph.append([S, E, -T])

        if(bellman_ford(1)):
            print("YES")
        else:
            print("NO")