import math
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
    return round(total_weight,2)
def calculate_distance(star1, star2):
    a = star1[0]-star2[0]
    b = star1[1]-star2[1]

    return math.sqrt((a*a)+(b*b))

if __name__ == "__main__":
    N = int(input())
    for i in range(1, N+1):
        make_set(i)
    arr = []
    for i in range(N):
        x, y = map(float, input().split())
        arr.append([x, y])
    graph = []
    for i in range(N-1):
        for j in range(i+1, N):
            graph.append((calculate_distance(arr[i], arr[j]), i+1, j+1))

    graph.sort()
    print(kruskal(graph))

