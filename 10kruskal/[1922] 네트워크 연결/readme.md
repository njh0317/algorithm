# 백준 1922번 : 네트워크 연결

## Algorithm

MST, Kruskal

## Description
1. find 함수 : v 의 최상위 정점을 찾는 함수
    ```python
    def find(v):
        if(parent[v]!=v):
            parent[v] = find(parent[v])
        return parent[v]
    ```
2. union 함수 : v, u 두 정점의 부모 노드를 찾아 연결해주는 함수
    ```python
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
    ```
## Review
크루스칼을 미리 공부해서 금방 풀었다.
