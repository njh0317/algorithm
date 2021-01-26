parent = {}
rank = {}
def make_set(v):
    parent[v] = v
    rank[v] = 0
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
def kruskal(graph):
    mst = []
    total_weight = 0

    for edge in graph:
        weight, u, v = edge
        if(find(u)!=find(v)):
            union(u, v)
            mst.append(edge)
            total_weight+=weight
    return total_weight
if __name__ == "__main__":
    N = int(input())
    M = int(input())
    for i in range(1, N+1):
        make_set(i)
    
    graph = []
    for i in range(M):
        v, u, weight = map(int, input().split())
        graph.append((weight, v, u))
        graph.append((weight, u, v))
    graph.sort()
    print(kruskal(graph))

