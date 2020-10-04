import sys
from itertools import combinations
def calculate_distance(list1, list2):
    return abs(list1[0]-list2[0])+abs(list1[1]-list2[1])
if __name__ == "__main__":
    N, M = map(int,sys.stdin.readline().split())
    home = []
    chicken = []

    for i in range(N):
        new_home = list(map(int,sys.stdin.readline().split()))
        for j in range(N):
            if(new_home[j]==1):
                home.append([i,j])
            elif(new_home[j]==2):
                chicken.append([i,j])
    
    hot_chicken = list(combinations(chicken,M))
    min_distance = 9999

    for now_chicken in hot_chicken:
        sum_distance = 0
        for j in home:
            small_distance = 9999
            for k in now_chicken:
                small_distance = min(small_distance, calculate_distance(j,k))
            sum_distance+=small_distance
        min_distance = min(min_distance, sum_distance)
    print(min_distance)