#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
using namespace std;
typedef struct{
    int y, x, t;
}st;
int MAXT = 50*50+1;
int N, M, map[50][50], empty_space;
vector<pair<int, int>> virus;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};
bool isin(int x, int y)
{
    if(0<=x && x<N && 0<=y && y<N) return true;
    return false;
}
int spread_virus(vector<pair<int, int>> &active_virus)
{
    int time = 0, check_empty = empty_space;
    bool visited[50][50];
    bool findflag = false;
    queue<st> q;
    memset(visited, false, sizeof(visited));
    for(auto& v:active_virus){
        q.push({v.first, v.second, 0});
        visited[v.first][v.second] = true;
    }
    
    while(!q.empty())
    {
        st top = q.front();
        q.pop();
        for(int i=0;i<4;i++)
        {
            int nexty = top.y + dy[i];
            int nextx = top.x + dx[i];
            if(isin(nextx, nexty)){
                if(map[nexty][nextx]!=1 && find(active_virus.begin(), active_virus.end(), make_pair(nexty, nextx))==active_virus.end() && !visited[nexty][nextx])
                {
                    time = max(time, top.t+1);
                    q.push({nexty, nextx, top.t+1});
                    visited[nexty][nextx] = true;
                    if(map[nexty][nextx] == 0) check_empty-=1;
                }
                if(check_empty == 0) {
                    findflag = true;
                    break;
                }
            }
        }
        if(findflag) break;
        
    }
    if(findflag) return time;
    else return -1;
}
void choose_virus(vector<pair<int, int>> &active_virus, int index){
    if(active_virus.size() == M){
        int time = spread_virus(active_virus);
        if(time!=-1) MAXT = min(MAXT, time);
        return;
    }
    for(int i=index;i<virus.size();i++){
        active_virus.push_back(virus[i]);
        choose_virus(active_virus, i+1);
        active_virus.pop_back();
    }
    return;
    
}
int main(){
    scanf("%d %d", &N, &M);
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
            cin>>map[i][j];
            if(map[i][j] == 2) virus.push_back(make_pair(i, j));
            else if(map[i][j] == 0) empty_space+=1;
        }
    }
    vector<pair<int, int>> active_virus;
    choose_virus(active_virus, 0);
    if(MAXT == 50*50+1) printf("-1");
    else printf("%d\n", MAXT);
    return 0;
}
