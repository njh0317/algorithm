parent = {}
rank = {}
mst = {}
def make_set(v):
    parent[v] = v
    rank[v] = 0
    mst[v] = {}
def find(v):
    if(parent[v]!=v):
        parent[v] = find(parent[v])
    return parent[v]
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    if(root1 != root2):
        if(rank[root1]> rank[root2]):
            parent[root2] = root1
        else:
            parent[root1] = root2
            if(rank[root1] == rank[root2]):
                rank[root2]+=1
def dfs(start, before_vertex):
    weight = 0

    now_node = mst[start]
    for a, b in now_node.items():
        if(a!=before_vertex):
            weight  = max(weight, dfs(a, start)+b)
    return weight
def kruskal(graph):
    total_weight = 0

    for edge in graph:
        weight, u, v = edge
        if(find(u)!=find(v)):
            union(u, v)
            mst[u][v] = weight
            mst[v][u] = weight
            total_weight+=weight
    return total_weight
if __name__ == "__main__":
    N, M = map(int,input().split())
    for i in range(N):
        make_set(i)
    graph = []
    for i in range(M):
        v, u, weight = map(int, input().split())
        graph.append((weight, v, u))
    graph.sort()
    print(kruskal(graph))
    check_weight = 0

    for i in range(N):
        check_weight = max(check_weight, dfs(i, -1))
    print(check_weight)



