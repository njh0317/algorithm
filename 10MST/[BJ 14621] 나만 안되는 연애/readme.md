# 백준 1922번 : 네트워크 연결

## Algorithm

MST, Prim

## Description
```
Kruskal 대신 Prim 을 선택한 이유는 정점 중심의 MST 였기 때문이다. 
최소 거리를 구할 때 조건이 남초 대학교와 여초 대학교를 연결지어야 했다. 
따라서 정점에 대한 정보를 이용해 최소거리를 만들어야한다. 
그렇기 때문에 간선을 이용하는 Kruskal 보단 Prim 이 적절하다고 생각했다.
```
1. `def prim(start, school_info)` : heapq 사용

    
## Review
프림과 크루스칼 모두 MST 이지만 문제 조건을 잘 확인하고 적절하게 골라 사용해야 한다.
