//
//  main.cpp
//  cpp
//
//  Created by 나지혜 on 2021/03/02.
//
#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;
const int MAX = 100001;
int V, E, cnt, dfsn[MAX];
vector<int> adj[MAX];
bool finished[MAX];
stack<int> S;
vector<vector<int>> SCC;
int Scnum;

int DFS(int v)
{
    dfsn[v] = ++cnt;
    S.push(v);
    int parent = dfsn[v];
    for(int next:adj[v]){
        if(dfsn[next] == 0)
        {
            parent = min(parent, DFS(next));
        }
        else if(!finished[next]){
            parent = min(parent, dfsn[next]);
        }
    }
    
    if(parent == dfsn[v])
    {
        vector<int> new_scc;
        while(1)
        {
            int top = S.top();
            S.pop();
            new_scc.push_back(top);
            finished[top] = true;
            if(top == v) break;
        }
        sort(new_scc.begin(), new_scc.end());
        SCC.push_back(new_scc);
        Scnum+=1;
    }
    return parent;
}

int main(){
    scanf("%d %d", &V, &E);
    for (int i=0; i<E; i++){
        int A, B;
        scanf("%d %d", &A, &B);
        adj[A].push_back(B);
    }
    for (int i=1; i<=V; i++)
    {
        if(dfsn[i] == 0){
            DFS(i);
        }
    }
    sort(SCC.begin(), SCC.end());
    
    printf("%d\n", Scnum);
    for(auto& curr: SCC)
    {
        for(int nowcurr:curr)
            printf("%d ", nowcurr);
        puts("-1");
    }
}
