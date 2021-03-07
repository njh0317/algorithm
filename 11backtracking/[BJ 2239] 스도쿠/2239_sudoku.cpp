#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
bool flag = false;
int arr[9][9];
vector<int> check_candidate(int i, int j){
    vector<int> candidate(10);
    //check row
    for(int k=0;k<9;k++){
        if(k!=j && arr[i][k]!=0){
            candidate[arr[i][k]] = 1;
        }
    }
    
    //check col
    for(int k=0;k<9;k++){
        if(k!=i && arr[k][j]!=0){
            candidate[arr[k][j]] = 1;
        }
    }
    
    //check 3*3
    int starti = i-i%3;
    int startj = j-j%3;
    
    for(int k = starti; k<starti+3; k++){
        for(int l = startj;l<startj+3; l++){
            if((i!=k && j!=l) && arr[k][l] != 0){
                candidate[arr[k][l]] = 1;
            }
        }
    }
    return candidate;
}
void backtracking(int y, int x, int zero_num){
    if(zero_num == 0){
        // 출력하고
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                printf("%1d", arr[i][j]);
            }
            puts("");
        }
        flag = true;
        return;
    }
    
    for(int i=0;i<9;i++){
        if(y>i) continue;
        for(int j=0;j<9;j++){
            if(y==i && x>j) continue;
            if(arr[i][j] == 0)
            {
                vector<int> candidate_list = check_candidate(i, j);
                int candi_count = 0;
                for(int k=1;k<10;k++){
                    if(candidate_list[k]==0){
                        candi_count+=1;
                        arr[i][j] = k;
                        backtracking(i, j+1, zero_num-1);
                        arr[i][j] = 0;
                        if(flag) break;
                    }
                }
                return;
            }
        }
    }
    return;
}
int main(){
    int zero = 0;
    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            scanf("%1d", &arr[i][j]);
            if(arr[i][j]==0) zero++;
        }
    }
    
    backtracking(0, 0, zero);
    
    return 0;
}
