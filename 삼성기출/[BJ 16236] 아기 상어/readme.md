# 백준 16236번 : 아기 상어

## Algorithm

BFS, Simulation

## Description

#### 기본 로직

arr : 공간 정보를 담고 있는 이차원 리스트

fsize : 물고기 크기별로 개수를 저장해주는 리스트

1) 현재 위치에서 더 이상 먹을 수 있는 물고기가 없으면 종료

2) 현재 위치에서 먹을 수 있는 가장 가까운 물고기를 BFS로 찾는다.

3) 그 위치로 이동


#### 함수 설명

1) bfs(arr,nowsize, ni, nj) : 현재 위치인 ni, nj 에서 현재 물고기 크기인 nowsize 보다 작은 물고기 중 가장 가까운 위치에 있는 물고기를 찾아서 그 위치와 움직인 거리를 return 

2) find_shark(arr, now_size, eat_num, ni, nj) : 


## Review

너무 힘들다 ㅠㅠ

설명 다시 
