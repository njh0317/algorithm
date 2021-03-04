# 백준 17142번 : 연구소 3

## Algorithm

BFS, Bruteforce

## Description

### 기본 로직

`map` : 공간 정보를 담고 있는 이차원 리스트

`empty_space` : 빈 공간(0)의 개수, 바이러스가 모두 퍼졌는지 여부를 확인하는데 사용

`virus` : 비활성 바이러스의 위치 정보를 저장하고 있는 벡터

1) 비활성 바이러스에서 M개의 활성 바이러스를 선택한다.

2) 선택된 바이러스를 시작으로 BFS로 바이러스를 퍼트린다.

### 함수 설명

**`void choose_virus(vector<pair<int, int>> &active_virus, int index)`** : 

+ active_virus에 backtracking 으로 선택된 바이러스 좌표를 담아준다.

+ active_virus의 size가 M 개이면 spread virus 함수 호출 

+ spread virus의 반환값이 -1이면 모든 칸에 바이러스를 퍼트리지 못했다.

+ spread virus의 반환값이 -1이 아니면 모든 칸에 바이러스를 퍼트렸기 때문에 MAXT(최단시간)와 비교해 최솟값을 저장한다.

**`int spread_virus(vector<pair<int, int>> &active_virus)`** : 

+ 활성 바이러스 active_virus를 시작으로 BFS를 사용해 바이러스를 퍼트린다.

+ 큐에는 좌표와 시간을 저장하는 구조체 st를 넣는다.

+ 빈 칸을 만날 때 마다 empty_space의 값이 저장된 check_empty 값을 하나씩 줄여준다.

    + 만약 check_empty 값이 0이 되면 모든 공간에 바이러스가 퍼졌다는 것을 의미하므로 더 진행하지 않고 종료한다.

+ BFS 진행 중 만나는 시간의 최댓값을 저장하고 있다가, while 문이 종료된 후에 check_empty 값이 0이라면 시간을 return한다.
       
## Review

저번 삼성 코테 대비때는 한 8번 도전해서 틀렸었는데 이번엔 1시간 만에 풀어냈다. 

성장한 것 같아 뿌듯하다.