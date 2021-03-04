#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
const int MAXK = 18; //2^17 > 100000
const int MAX = 100001;
using namespace std;
int N, M;
vector<int> adj[MAX]; //초기 graph 저장용
int parent[MAX][MAXK];
int depth[MAX];
void make_tree(int now_vertex, int count)
{
    for(int next_vertex:adj[now_vertex]){
        if(depth[next_vertex] == -1){
            parent[next_vertex][0] = now_vertex;
            depth[next_vertex] = count+1;
            make_tree(next_vertex, count+1);
        }
    }
    
}
void fill_parent(){
    for(int j=0;j<MAXK-1;j++){
        for(int i=0;i<N;i++){
            if(parent[i][j] != -1) parent[i][j+1] = parent[parent[i][j]][j];
        }
    }
    
}
int find_LCA(int u, int v) //u의 depth 가 v 보다 크다.
{
    int depth_diff = depth[u]-depth[v];
    if(depth_diff != 0)
    {
        for(int i = 0; depth_diff; i++){
            if(depth_diff%2) u = parent[u][i];
            depth_diff/=2;
        }
    }
    if(u!=v){
        for(int i=17;i>-1;i--)
        {
            if(parent[u][i] != -1 && parent[u][i]!=parent[v][i])
            {
                u = parent[u][i];
                v = parent[v][i];
            }
        }
        u = parent[u][0];
    }
    
    return u+1;
}
int main()
{
    scanf("%d", &N);
    memset(parent, -1, sizeof(parent));
    fill_n(depth, N, -1);
    for(int i=0;i<N-1;i++)
    {
        int x, y;
        scanf("%d %d", &x, &y);
        x-=1;
        y-=1;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }
    depth[0] = 0;
    make_tree(0, 0);
    fill_parent();
    
    scanf("%d", &M);
    vector<int> answer;
    for(int i=0;i<M;i++)
    {
        int u, v;
        scanf("%d %d", &u, &v);
        u-=1; v-=1;
        if(depth[u]<depth[v]) swap(u, v);

        answer.push_back(find_LCA(u, v));
    }
    for(int ans:answer) printf("%d\n", ans);
    return 0;
}
