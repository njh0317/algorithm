import sys
from itertools import accumulate
if __name__ == "__main__":
    N, M = map(int, input().split())
    numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    for i in range(N):
        numbers[i] = list(accumulate(numbers[i]))

    for i in range(1, N):
        for j in range(N):
            numbers[i][j] += numbers[i-1][j]

    for i in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        minus1 = 0 if y1-2 <0 else numbers[x2-1][y1-2]
        minus2 = 0 if x1-2 <0 else numbers[x1-2][y2-1]
        plus = 0 if x1-2<0 or y1-2<0 else numbers[x1-2][y1-2]
        print(numbers[x2-1][y2-1]-minus1-minus2+plus)
# 시간초과 -> 다시풀기 