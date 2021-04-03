#include <iostream>
#include <cstring>
int N;
int cache[1001][2][3];//day, 지각, 결석
int check(int day, int late_num, int absent_num){
    if(day == N) return 1;
    int &ret = cache[day][late_num][absent_num];
    if(ret != -1) return ret;
    ret = 0;
    ret+=check(day+1, late_num, 0);
    if(late_num<1) ret+=check(day+1, late_num+1, 0);
    if(absent_num<2) ret+=check(day+1, late_num, absent_num+1);
    return ret%=1000000;
}
int main(){
    scanf("%d", &N);
    memset(cache, -1, sizeof(cache));
    int answer = check(0, 0, 0);
    printf("%d", answer);
    return 0;
}
