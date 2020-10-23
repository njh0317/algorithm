
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
int N, K;
vector<string> arr[1001];
int main()
{
    cin>>N;
    string temp;
    for(int i=0;i<N;i++)
    {
        cin>>K;
        for (int j = 0;j<K;j++)
        {
            cin>>temp;
            arr[i].push_back(temp);
        }
    }
    //입력 받기 완료 

    sort(arr, arr+N);


    vector<string> stack;
    for(int i=0;i<N;i++)
    {
        int count = 0;
        for (int j=0;j<stack.size() && j<arr[i].size();j++)
        {
            if(stack[j] == arr[i][j])
            {
                count++;
            }
            else
            {
                break;
            }
        }

        int size = stack.size();
        for(int j = count;j<size;j++)
        {
            stack.pop_back();
        }
        for (int j = count; j <arr[i].size();j++)
        {
            for(int k = 0;k<stack.size();k++)
            {
                cout<<"--";
            }
            cout<<arr[i][j]<<"\n";
            stack.push_back(arr[i][j]);
        }
    }

    return 0;

}