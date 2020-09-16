from collections import deque

N,M,K,X = map(int, input().split(" "))

city_list = [[] for i in range(0, N+1)]
check_list = [9999999 for i in range(0,N+1)]
check_list[X] = 0

for i in range(0, M):
    a,b = map(int,input().split(" "))
    city_list[a].append(b)

answer = []

def bfs(start):
    queue = deque([start])

    while(queue):
        a = queue.popleft()
        print(city_list[a])
        for i in city_list[a]:

            check_list[i] = min(check_list[a]+1, check_list[int(i)])
            if check_list[i] == K:
                answer.append(i)
                break;
            if i not in queue:
                queue.append(i)
            print(check_list)
            a = input()
bfs(X)
flag = 0
print(answer)
# for i in range(1, len(check_list)):
#     if(i==X):
#         continue
#     if(check_list[i] == K):
#         print(i)
#         flag = 1
# if(flag == 0):
#     print(-1)


