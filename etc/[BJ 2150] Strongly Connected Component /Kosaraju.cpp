//
//  main.cpp
//  cpp
//
//  Created by 나지혜 on 2021/03/02.
//
#include <string.h>
#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;
const int MAX = 100001;
int V, E;
vector<int> adj[MAX];
vector<int> reverse_adj[MAX];
bool visited[MAX];
stack<int> S;
vector<vector<int>> SCC;
vector<int> new_scc;
int Scnum;
void DFS(int v)
{
    for(int next:adj[v])
    {
        if(!visited[next])
        {
            visited[next] = true;
            DFS(next);
        }
    }
    S.push(v);
    return;
}
void reverse_DFS(int v)
{
    new_scc.push_back(v);
    for(int next:reverse_adj[v])
    {
        if(!visited[next])
        {
            visited[next] = true;
            reverse_DFS(next);
        }
    }
    return;
}
int main(){
    scanf("%d %d", &V, &E);
    for (int i=0; i<E; i++){
        int A, B;
        scanf("%d %d", &A, &B);
        adj[A].push_back(B);
        reverse_adj[B].push_back(A);
    }
    for (int i=1; i<=V; i++)
    {
        if(!visited[i])
        {
            visited[i] = true;
            DFS(i);
        }
    }
    memset(visited, false, sizeof(visited));
    while(!S.empty())
    {
        int top = S.top();
        S.pop();
        if(!visited[top])
        {
            new_scc.clear();//모든 원소 삭제
            visited[top] = true;
            reverse_DFS(top);
            sort(new_scc.begin(), new_scc.end());
            SCC.push_back(new_scc);
            Scnum+=1;
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
