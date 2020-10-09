# 백준 19236번 : 청소년 상어

## Algorithm

Simulation, Backtracking

## Description

#### 기본 로직
1. 물고기 이동
2. 상어가 물고기 먹기

#### 함수 설명
1. change_dir(num) : 현재 방향을 num 파라미터로 받아서 변경된 방향을 반환해준다.

2. change_fish_position(arr) : 현재 물고기의 위치 arr를 파라미터로 받아서 물고기 번호 순서대로 이동시켜준다.

3. make_eat_list(arr, ni, nj, ndir) : 현재 상어의 위치와 뱡항을 파라미터로 받아서 상어가 갈 수 있는 위치를 리스트로 반환해준다.
  + 종료조건 : 가다가 벽을 만나면 종료

4. backtracking(arr, ni, nj, ndir, eat) : 먹을 수 있는 최대 물고기 크기를 찾는 백트래킹 함수
+ 파라미터

  arr : 현재 물고기의 위치 정보를 저장하고 있는 이차원 리스트
  
  ni, nj, ndir : 현재 상어의 위치와 방향
  
  eat : 현재까지 먹은 물고기의 양
  
+ 설명
  + 물고기의 위치를 이동시킨다 : change_fish_position 호출
  
  + 현재 상어 위치에서 먹을 수 있는 물고기 위치를 찾아준다. : make_eat_list 호출
  
    + 만약에 make_eat_list를 호출해서 반환받은 리스트의 길이가 0이라면, 즉 상어가 갈 수 없는 곳이 없다면
      + 현재 먹은 물고기 크기와 최대 값을 비교해서 최대값을 변경해준다.
      + 종료 조건
    + 갈 수 있는 곳이 있다면, make_eat_list를 돌면서 방문해준 후 backtracking 다시 호출
      + 주의! 현재 상태를 저장해준 후 상어를 이동시키고 backtracking 호출 해준다.
      + 호출이 끝난 후에는 다시 원상태로 복구 해준다.
 5. main
 + backtracking(fish, 0, 0, shark_dir, eat) 호출


## Review

아기 상어보다는 훨씬 빨리 풀었다.

필요한 기능별로 함수를 미리 잘 구현해놔서 사용만 하면 됐기 때문에 편했다.
