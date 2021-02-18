import math
import itertools
def calculate(point1, point2):
    return math.sqrt(float((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2))
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        vector = []
        total_x = 0
        total_y = 0
        answer = float('inf')
        for j in range(N):
            x, y = map(int, input().split())
            total_x += x
            total_y += y
            vector.append([x, y])
        comb = list(itertools.combinations(vector, int(N/2)))

        for j in range(int(len(comb)/2)):
            x1, y1 = 0, 0
            one_comb = list(comb[j])
            for point in one_comb:
                x1 += point[0]
                y1 += point[1]
            x2 = total_x - x1
            y2 = total_y - y1
            answer = min(answer, calculate([x1, y1],[x2, y2]))
        print(answer)


        
