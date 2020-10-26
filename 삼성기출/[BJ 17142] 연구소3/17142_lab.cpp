#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <memory.h>
using namespace std;

typedef struct
{
    int x;
    int y;
    int time;
}st;
int dx[4] = {0,0,-1,1}; //상하좌우
int dy[4] = {-1,1,0,0}; // 
int N, M;
int zero_num = 0;
vector<st> virus_list;
int min_time = 999999;
int arr[50][50];
bool isIn(int x, int y)
{
    if(0>x||x>=N) return false;
    if(0>y||y>=N) return false;
    if(arr[y][x] == 1) return false;
    return true;
}
bool isVirus(int x, int y)
{
    for(int i=0;i<virus_list.size();i++)
    {
        if(virus_list[i].x == x and virus_list[i].y == y)
        {
            return true;
        }
    }
    return false;
}
void active_virus(vector<int> num_list)
{
    int visited[N][N];
    memset(visited, 0, sizeof(visited));

    queue<st> q;
    for(int i=0;i<num_list.size();i++)
    {
        st new_node;
        new_node.x = virus_list[num_list[i]].x;
        new_node.y = virus_list[num_list[i]].y;
        new_node.time = virus_list[num_list[i]].time;
        q.push(new_node);
        visited[virus_list[i].y][virus_list[i].x] = 1;
    }
    int max_time = 0;
    while(!q.empty())
    {
        st node = q.front();
        q.pop();
        int x = node.x;
        int y = node.y;
        int time = node.time;
        
        // if(!isVirus(x, y))
        // {
        //     
        // }
        if(arr[y][x] != 2) zero_num-=1;
        if(zero_num == 0) 
        {
            max_time = max(max_time, time);
            break;
        }
        // for(int i=0;i<5;i++)
        // {
        //     for(int j=0;j<5;j++)
        //     {
        //         cout<<visited[i][j]<<" ";
        //     }
        //     cout<<""<<endl;
        // }
        // cout<<""<<endl;
        
        for(int i=0;i<4;i++)
        {
            int nextx = x + dx[i];
            int nexty = y + dy[i];

            if(isIn(nextx, nexty) and visited[nexty][nextx]==0)
            {
                visited[nexty][nextx] = 1;
                st new_node;
                new_node.x = nextx;
                new_node.y = nexty;
                new_node.time = time+1;
                q.push(new_node);
            }
        }

    }
    if(zero_num == 0)
        min_time = min(min_time, max_time);

}
void make_comb(int nownum, int prev, vector<int> num_list, int new_zero)
{
    if(nownum == M)
    {
        //호출 
        zero_num = new_zero;
        active_virus(num_list);
        return;
    }

    for(int i=prev;i<virus_list.size();i++)
    {
        num_list.push_back(i);
        make_comb(nownum+1, i+1, num_list, new_zero);
        num_list.pop_back();
    }

}
int main()
{
    cin>>N>>M;
    int temp;
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
            cin>>temp;
            arr[i][j] = temp;
            if(temp == 0) zero_num+=1;
            if(temp == 2) 
            {
                st new_node;
                new_node.x = j;
                new_node.y = i;
                new_node.time = 0;
                virus_list.push_back(new_node);
            }
        }
    }
    int 
    new_zero_num = zero_num;
    vector<int> num_list;
    make_comb(0, 0, num_list, new_zero_num);
    if(min_time == 999999)
        cout<<-1<<endl;
    else
        cout<<min_time<<endl;
    // for(int i=0;i<N;i++)
    // {
    //     for(int j=0;j<N;j++)
    //     {
    //         cout<<arr[i][j];
    //     }
    //     cout<<""<<endl;
    // }
    return 0;
}
