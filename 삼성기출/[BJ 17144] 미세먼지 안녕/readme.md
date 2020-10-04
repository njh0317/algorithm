# 삼성기출/백준 17144번 : 미세먼지 안녕

## Algorithm

Simulation

## Description

1. 처음 접근법(재귀)
  + DFS 풀 듯이 풀었다.
    + 퍼지려고 하는 위치에 이미 미세먼지가 존재한다면, 전달 될 미세먼지 양을 파라미터로 가져가서 그 위치에서 퍼지는 미세먼지 양을 계산해준다.
    + 그 후, 파라미터 값을 더해주고 현재 위치의 미세먼지 또한 이전 위치로 퍼질 것이므로 이 미세먼지 양을 return 해준다.
    
  ``` python
  def spread(r, c, spread_dust): #재귀로 짠 것
    visited[r][c]=1 #방문 표시해주고
    num = 0
    dust = room[r][c]//5
    if(dust == 0):
        room[r][c]+=spread_dust
        return 0
    for i in range(4):
        nextR = r + dr[i]
        nextC = c + dc[i]
        if(nextR<R and nextC<C and nextR>=0 and nextC>=0):
            if(room[nextR][nextC] > -1):
                num+=1 # spread 되는 공간의 수 세아려줌
                if (room[nextR][nextC]!=0 and visited[nextR][nextC]==0): # 퍼지려는 공간에 이미 미세먼지가 있다면
                    spread(nextR, nextC, dust)
                else: 
                    room[nextR][nextC] += dust
                    visited[nextR][nextC] = 1 #방문 표시해줌
    room[r][c]+=spread_dust
    room[r][c]-=num*dust
    return dust
  ```
2. 이 후 접근법
  + 모든 위치를 확인 하면서, 미세먼지가 있다면 그 주위를 돌면서 퍼지는 양을 visited 에 더해준다.
  
  + 퍼진다면 현재 위치의 미세 먼지 양은 빼준다.
  
  + 마지막에 한번 더 확인하며 visited 의 값들을 room 에 더해준다.
  ``` python
  def spread2():
    visited = [[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if(room[i][j]>=5):
                dust = room[i][j]//5
                for k in range(4):
                    nextR = i + dr[k]
                    nextC = j + dc[k]
                    if(nextR<R and nextC<C and nextR>=0 and nextC>=0 and room[nextR][nextC]!=-1):
                        room[i][j]-=dust
                        visited[nextR][nextC]+=dust
    
    for i in range(R):
        for j in range(C):
            room[i][j]+=visited[i][j]
  ```

  

## Review

처음에 재귀로 짰을 때 너무 만족스러운 코드였는데,, 시간 초과나서 슬펐다..

python은 매우 느리기 때문에 시간초과가 되는 경우에 pypy 를 쓰면 됐었는데 pypy 는 재귀에 약하다는 특징이 있다.

그래서 첫 결과는 둘다 시간초과, 메모리초과, 런타임 에러.. 등등 다양한 에러가 났다...

코드를 고치지 않을 수 없었다..

