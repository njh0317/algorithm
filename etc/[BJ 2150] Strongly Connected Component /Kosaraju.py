import sys
sys.setrecursionlimit(10**9)
scc = []
graph = {}
reverse_graph = {}
stack = []
new_scc = []
def init(v):
    graph[v] = []
    reverse_graph[v] = []
def DFS(v):
    for node in graph[v]:
        if(dfs_visited[node] == False):
            dfs_visited[node] = True
            DFS(node)
    stack.append(v)
    return

def reverse_DFS(v):
    new_scc.append(v)
    for node in reverse_graph[v]:
        if(dfs_visited[node] == False):
            dfs_visited[node] = True
            reverse_DFS(node)

    return
if __name__ == "__main__":
    V, E = map(int, input().split())
    for i in range(1, V+1):
        init(i)
    for i in range(E):
        A, B = map(int, input().split())
        graph[A].append(B)
        reverse_graph[B].append(A)
    dfs_visited = [False]*(V+1)
    for i in range(1, V+1):
        if(dfs_visited[i] == False):
            dfs_visited[i] = True
            DFS(i)
    dfs_visited = [False]*(V+1)
    while(stack):
        vertex = stack.pop()
        if(dfs_visited[vertex] == False):
            new_scc = []
            dfs_visited[vertex] = True
            reverse_DFS(vertex)
            new_scc.sort()
            scc.append(new_scc)
    scc.sort()
    print(len(scc))
    for i in scc:
        for k in i:
            print(k, end = " ")
        print(-1)
