# 백준 14501 : 퇴사

## Algorithm

Dynamic Programming

## Description

배열을 거꾸로 채워간다고 생각하고 진행했다.

1. 현재 날짜에 현재 할 수 있는 상담이 걸리는 기간을 더했을 때 N을 넘어가면 할 수 없는 상담이기 때문에 continue

2. 오늘 진행 하는 상담일수 이후 날짜(예, 오늘이 3일이고 오늘 상담이 2일 걸리면 5일 부터 끝까지)중의 최대 비용에 오늘 상담 비용 값을 넣어준다.

``` python
    money[i] = max(money[i+work[i][0]:])+work[i][1]
```
