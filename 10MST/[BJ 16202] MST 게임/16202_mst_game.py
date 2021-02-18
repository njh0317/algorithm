##Kruskal
parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

def union(v, u):
    root1 = find(v)
    root2 = find(u)

    if(root1 != root2):
        if(rank[root1]>rank[root2]):
            parent[root2] = root1
        else:
            parent[root1] = root2
            if(rank[root1]==rank[root2]):
                rank[root1]+=1
        
def find(v):
    if(parent[v]==v):
        return v
    else:
        return find(parent[v])

def kruskal(graph):
    mst = []
    min_weight = 0

    for edge in graph:
        weight, u, v = edge
        if(find(v)!=find(u)):
            union(v, u)
            mst.append(edge)
            min_weight+=weight
    return mst, min_weight

if __name__ == "__main__":
    graph = []
    N, M, K = map(int, input().split())
    
    for i in range(1, M+1):
        u, v = map(int, input().split())
        graph.append((i, u, v))
    graph.sort()
    answer = []
    for i in range(K):
        if(M-i<N-1):
            print("0", end = " ")
            continue
        for i in range(1, N+1):
            make_set(i)
        mst, min_weight = kruskal(graph)
        
        if(len(mst)!=N-1):
            print("0", end = " ")
        else:
            print(str(min_weight), end = " ")
        graph.remove(mst[0])
