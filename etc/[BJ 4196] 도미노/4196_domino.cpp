//
//  main.cpp
//  4196
//
//  Created by 나지혜 on 2021/03/03.
//
#include <cstdio>
#include <cstring>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;
const int MAX = 100001;
int N, dfsn[MAX], sccnum, check, answer[MAX];
stack <int> S;
bool finished[MAX];
vector<int> adj[MAX];
int DFS(int v)
{
    dfsn[v] = ++check;
    S.push(v);
    int parent = dfsn[v];
    for(int next:adj[v])
    {
        if(dfsn[next] == 0)
        {
            parent = min(parent, DFS(next));
        }
        else if(!finished[next])
        {
            parent = min(parent, dfsn[next]);
        }
    }
    
    if(parent == dfsn[v])
    {
        while(1)
        {
            int top = S.top();
            S.pop();
            finished[top] = true;
            answer[top] = sccnum;
            if(top == v) break;
        }
        sccnum+=1;
    }
    
    return parent;
}
int main()
{
    int TC, M;
    
    scanf("%d", &TC);
    for(int t;t<TC;t++)
    {
        scanf("%d %d", &N, &M);
        for(int i=1; i<=N;i++)
        {
            adj[i].clear();
        }
        memset(finished, false, sizeof(finished));
        memset(dfsn, 0, sizeof(dfsn));
        memset(answer, 0, sizeof(answer));
        sccnum = 0;
        check = 0;
        
        for(int i=0;i<M;i++)
        {
            int x, y;
            scanf("%d %d",&x, &y);
            adj[x].push_back(y);
        }
        
        for(int i=1;i<=N;i++)
        {
            if(dfsn[i] == 0)
                DFS(i);
        }
        int sccindegree[MAX] = {0};
        for(int i=1;i<=N;i++)
        {
            for(int next:adj[i])
            {
                if(answer[i]!=answer[next])
                {
                    sccindegree[answer[next]]+=1; //들어가는 쪽의 scc indegree 증가
                }
            }
        }
        int domino = 0;
        for(int i=0;i<sccnum;i++)
        {
            if(sccindegree[i] == 0) domino+=1;
        }
        printf("%d\n", domino);
    }
    return 0;
}

