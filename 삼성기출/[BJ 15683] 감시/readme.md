# 백준 15683번 : 감시

## Algorithm

Simulation, Brute Force

## Description

1. CCTV_info(num) : CCTV 숫자마다 가능한 방향 정보를 리스트로 반환해준다.

2. isInarr(nowc,nowr) : arr 를 벗어나지 않고, 벽이 아니면 True 반환

3. DFS(nownum, cctv_list, choose_list) : CCTV 목록을 DFS로 돌면서 가능한 방향 조합을 찾아서 각 조합에 대해 cctv 상황을 확인해주는 checkarr 호출한다.
#### 파라미터

+ nownum : 현재까지 확인한 cctv 의 개수
+ cctv_list : 모든 cctv 의 위치와 번호 정보를 담고있는 리스트
+ choose_list : 각 cctv 마다 할 수 있는 방향이 여러 개 이기 때문에, 어떤 방향을 선택했는지를 담아주는 리스트

#### 시퀀스 

+ 확인한 cctv의 개수와 전체 cctv 개수가 같으면, 즉 모든 cctv를 확인했으면, checkarr 를 호출해서 이 상황에 대해 사각지대 개수를 확인해주고 종료

+ 현재 확인하는 cctv가 가능한 방향 목록을 CCTV_info 를 호출해 dir_list 에 담아준다.

  + dir_list 를 돌면서 하나씩 선택해서 choose_list 에 append 해주고, DFS를 다시 호출한다.
  + 하나 확인이 끝나면 choose_list 에 마지막 요소를 다시 없애준다.

4. checkarr(cctv_list, choose_list) : cctv정보를 담은 cctv_list 와 모든 cctv가 어떤 방향을 가지고 있는지 담은 choose_list를 파라미터로 받아서 이 상황에 대해 사각지대의 개수를 확인해 반환해준다.
+ cctv_list 의 i 번째 cctv 는 choose_list 의 i 번째 방향을 가지고 있다.

+ cctv i 마다, 또 한 cctv 가 여러개의 방향을 가질 수 있기 때문에 각 방향 j 마다 cctv 가 감시할 수 있는 곳이면 -1 을 표시해준다.

+ arr 의 0 의 개수를 확인해주면, 그 곳이 바로 사각지대이다.
