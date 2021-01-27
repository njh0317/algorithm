parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0
def make_minus(v):
    parent[v] = -1
    rank[v] = 0
def find(v):
    if(parent[v] == -1):
        return -1
    elif(parent[v]==v):
        return v
    else:
        return find(parent[v])
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    if(root1 != root2):
        if(root1 == -1):
            parent[root2] = root1
        elif(root2 == -1):
            parent[root1] = root2
        else:
            parent[root2] = root1
def isAllconnected():
    for i in parent:
        if(i!=-1):
            return False
    return True

def kruskal(graph):
    mst = []
    total_weight = 0

    for edge in graph:
        weight, u, v = edge
        if(find(u)!=find(v)):
            union(u, v) 
            mst.append(edge)
            total_weight+=weight
        if(isAllconnected()):
            return mst, total_weight
    
    return mst, total_weight
if __name__ =="__main__":
    N, M, K = map(int, input().split())
    point = list(map(int, input().split()))
    point_graph = []
    graph = []
    for i in range(N):
        if((i+1) in point):
            make_minus(i+1)
        else:
            make_set(i+1)
    for i in range(M):
        u, v, w = map(int, input().split())
        graph.append((w, u, v))
    
    graph.sort()
    answer, weight = kruskal(graph)
    print(weight)

