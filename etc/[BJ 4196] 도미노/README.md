# 백준 4196번 : 도미노 

## Algorithm

강한 연결 요소

## Description

1. 타잔 알고리즘을 사용해 SCC를 찾는다. 이 때, 이전에 풀었던 문제처럼 SCC끼리 저장하지 않고, 1차원 배열에 SCC 번호를 저장한다. (같은 숫자 끼리는 같은 scc)

2. SCC 끼리 위상정렬을 한다. 이 말이 무슨 말이냐 하면, SCC 묶음을 하나의 노드로 보고 위상정렬 하듯 indegree를 확인한다. SCC로 들어오는 엣지가 없다면, 즉 indegree가 0이라면 다른 도미노에 의해 이 SCC가 넘어지는 경우는 없다. 따라서 수동으로 넘어뜨려줘야한다.

    ```cpp
    int sccindegree[MAX] = {0};
    for(int i=1;i<=N;i++)
    {
        for(int next:adj[i])
        {
            // 간선 i->next에 대해, i와 next가 다른 SCC에 속하면 next가 속한 SCC의 outdegree++
            if(answer[i]!=answer[next])
            {
                sccindegree[answer[next]]+=1; //들어가는 쪽의 scc indegree 증가
            }
        }
    }

    ```
3. indegree가 0인 SCC의 개수를 확인한다.


## Review

공부하고 푸니까 쉽다. 

근데 cpp로 푸니까 아직 적응이 안돼서 푸는데 시간이 좀 걸린다!