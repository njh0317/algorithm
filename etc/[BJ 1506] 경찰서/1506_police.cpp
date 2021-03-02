#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;
const int MAX = 101;
int N, dfsn[MAX], cnt;
bool finished[MAX];
vector<int> cost;
vector<vector<int>> arr;
vector<vector<int>> SCC;
stack<int> S;

int dfs(int v)
{
    dfsn[v] = ++cnt;
    S.push(v);
    int parent = dfsn[v];
    for(int i=0;i<N;i++)
    {
        if(arr[v][i] == 1) //연결되어있으면
        {
            if(dfsn[i] == 0) //방문한적이 없으면
            {
                parent = min(parent, dfs(i));
            }
            else if(!finished[i])
            {
                parent = min(parent, dfsn[i]);
            }
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
        SCC.push_back(new_scc);
    }
    return parent;
}

int main(){
    scanf("%d\n", &N);
    string strInput;
    getline(cin, strInput);
    
    string strNum = "";
    for(int i=0;i<strInput.length();i++)
    {
        if(strInput.at(i) == ' ')
        {
            //공백을 만나면
            //공백을 만나기 전 까지 저장한 문자를 숫자로 바꾼 후 추가
            cost.push_back(atoi(strNum.c_str()));
            strNum = "";
        }
        else{
            //띄어쓰기가 나올 때까지 문자를 더한다.
            strNum+=strInput.at(i);
        }
    }
    //마지막 숫자도 벡터에 추가
    cost.push_back(atoi(strNum.c_str()));
    
    int num = 0;
    for(int i=0;i<N; i++)
    {
        vector<int> newarr;
        for(int j=0;j<N;j++)
        {
            scanf("%1d", &num);
            newarr.push_back(num);
        }
        arr.push_back(newarr);
    }

    for(int i=0;i<N;i++)
    {
        if(dfsn[i] == 0)
        {
            dfs(i);
        }
    }
    int answer = 0;
    for(auto& curr: SCC)
    {
        int check_answer = 1000001;
        for(int nowcurr:curr)
            check_answer = min(check_answer, cost[nowcurr]);
        answer+=check_answer;
    }
    printf("%d", answer);
}
