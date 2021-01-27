import heapq
from collections import defaultdict
visited = {}
distances = {}
real_graph = defaultdict(list)
graph = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
'edges': [
    (7, 'A', 'B'),
    (5, 'A', 'D'),
    (7, 'B', 'A'),
    (8, 'B', 'C'),
    (9, 'B', 'D'),
    (7, 'B', 'E'),
    (8, 'C', 'B'),
    (5, 'C', 'E'),
    (5, 'D', 'A'),
    (9, 'D', 'B'),
    (7, 'D', 'E'),
    (6, 'D', 'F'),
    (7, 'E', 'B'),
    (5, 'E', 'C'),
    (15, 'E', 'D'),
    (8, 'E', 'F'),
    (9, 'E', 'G'),
    (6, 'F', 'D'),
    (8, 'F', 'E'),
    (11, 'F', 'G'),
    (9, 'G', 'E'),
    (11, 'G', 'F'),
    ]
}
def make_set(v):
    visited[v] = False
    distances[v] = float('inf')

def prim(start):
    queue = []
    visited[start] = True
    distances[start] = 0
    mst = []
    for edge in real_graph[start]:
        heapq.heappush(queue, edge)
    
    while(queue):
        weight, x1, x2 = heapq.heappop(queue)
        if(visited[x2] == False):
            visited[x2] = True
            distances[x2] = weight
            mst.append((weight, x1, x2))
            for edge in real_graph[x2]:
                heapq.heappush(queue, edge)
    return mst
if __name__ == "__main__":
    vertices = graph['vertices']
    for vertex in vertices:
        make_set(vertex)
    edges = graph['edges']

    for edge in edges:
        weight, u, v = edge
        real_graph[u].append((weight, u, v))
    print(real_graph)
    print(prim('A'))
    print(distances)
