# 백준 2150번 : Strongly Connected Component

## Algorithm

강한 연결 요소

## Description

**강한 연결 요소를 풀기 위한 알고리즘은 2가지가 있다.**

**`타잔 알고리즘(Tarjan's Algorithm)`**

+ DFS와 stack 사용 

**`코사라주 알고리즘(Kosaraju Algorithm)`**

+ 주어진 그래프와 주어진 그래프의 역방향을 가지는 역방향 그래프, 스택을 사용한다.

+ DFS 2번

## Review

똑같은 로직인데 타잔과 코사라주 둘 다 python 은 통과 못하고(메모리 초과) c++로는 통과했다.. ㅠㅠ 
