# 백준 2638 : 치즈

## Algorithm

구현, 시뮬레이션

## Description

## Review

시간초과를 냈던 불필요한 구현 

1. 외부 공기와 내부 공기를 분리할 때 처음엔 외부공기를 모두 확인하고, 방문하지 않은 곳들을 모두 내부 공기로 바꿔주는 식(2이상의 숫자로 바꿔줌)으로 했었는데 굳이 이렇게 할 필요가 없었다. 그냥 처음에 외부 공기를 확인하면서 외부 공기를 다른 숫자로 바꿔주면 됐었다. 

2. 외부 공기를 확인할 때, 외부 공기도 여러 개로 분리되어있다고 생각해서, BFS로 외부공기를 한 번 확인 하고 나서도 다른 곳에 있는지 확인하는 작업을 거쳤다. 근데 조건에서 가장자리에는 치즈가 없다고 했기 때문에 한 번의 외부 공기 확인으로 외부 공기는 한 번에 확인이 된다.

**불필요한 작업 줄이자**