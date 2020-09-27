N = int(input())
food = list(map(int, input().split()))
ant = []

ant.append(food[0])
ant.append(food[1])
#4ant.append(food[0]+food[2])
for i in range(2, N):
    max_of_ant = max(ant[:-1])
    ant.append(max_of_ant+food[i])
print(ant)

