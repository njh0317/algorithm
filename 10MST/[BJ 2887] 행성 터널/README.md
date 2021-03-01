# 백준 2887번 : 행성 터널 

## Algorithm

MST, Kruskal

## Description

1. N의 최대 갯수가 100000개 이므로 모든 node를 연결할 수는 없다. 따라서 x, y, z에 대해 정렬해 인접한 점들끼리만 연결해준다.

    ```python
    for i in range(3): #x, y, z에 대해 정렬 
        tunnel.sort(key = lambda x:x[i])
        for k in range(N-1):
            graph.append((abs(tunnel[k][i] - tunnel[k+1][i]),tunnel[k][3], tunnel[k+1][3]))
    ```

2. 연결된 노드를 kruskal을 이용해 MST를 찾는다.

## Review
