parent = {}
rank = {}
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    if(root1 != root2):
        if(rank[root1]>rank[root2]):
            parent[root2] = root1
        else:
            parent[root1] = root2
            if(rank[root1]==rank[root2]):
                rank[root2]+=1
    return
def find(v):
    if(parent[v]!=v):
        parent[v] = find(parent[v])
    return parent[v]
def kruskal(graph):
    total_weight = 0

    for edge in graph:
        weight, v1, v2 = edge
        if(find(v1)!= find(v2)):
            total_weight+=weight
            union(v1, v2)
    
    return total_weight

def init(v):
    parent[v] = v
    rank[v] = 0
if __name__ == "__main__":
    N = int(input())
    tunnel = []
    graph = []
    for i in range(N):
        init(i)
        x, y, z = map(int, input().split())
        tunnel.append((x, y, z, i))

    for i in range(3):
        tunnel.sort(key = lambda x:x[i])
        for k in range(N-1):
            graph.append((abs(tunnel[k][i] - tunnel[k+1][i]),tunnel[k][3], tunnel[k+1][3]))
    graph.sort()
    # print(graph)
    print(kruskal(graph))