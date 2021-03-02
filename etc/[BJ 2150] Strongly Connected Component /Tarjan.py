#타잔알고리즘 -> 메모리초과 
import sys
sys.setrecursionlimit(10**9)
graph = {}
dfsn = {}
finished = {}
stack = []
scc = []
index = 0
def init(v):
    graph[v] = []
    dfsn[v] = -1
    finished[v] = False
def DFS(v):
    global index
    index+=1
    dfsn[v] = index
    stack.append(v)
    #자신의 dfsn, 자식들의 결과나 dfsn 중 가장 작은 번호를 parent에 저장 
    parent = dfsn[v]
    for vertex in graph[v]:
        if(dfsn[vertex] == -1):#방문한 적이 없으면 
            parent = min(parent, DFS(vertex))
        else:
            if(finished[vertex] == False): #방문은 했으나 아직 SCC로 추출되지 않은 상태(역방향 간선?)
                parent = min(parent, dfsn[vertex])
    #자신과 자신의 자손들이 도달가능한 제일 높은 정점이 자신일 경우 SCC 추출
    if(parent == dfsn[v]):
        new_scc = []
        while(True):
            top = stack.pop()
            new_scc.append(top)
            finished[top] = True
            if(top == v):
                break
        new_scc.sort()
        scc.append(new_scc)
    return parent
if __name__ == "__main__":
    V, E = map(int, input().split())
    for i in range(1, V+1):
        init(i)
    for i in range(E):
        A, B = map(int, input().split())
        graph[A].append(B)
    
    for i in range(1, V+1):
        if(dfsn[i] == -1):
            DFS(i)
    
    scc.sort()
    print(len(scc))
    for i in scc:
        for k in i:
            print(k, end = " ")
        print(-1)
