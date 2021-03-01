adj_list = {}

def init(v):
    adj_list[v] = []
def topological_sort():
    indegree = [0]*(N+1)
    answer = []

    for i in range(1, N+1):
        for j in range(1, N+1):
            temp = adj_list[j]
            for k in range(len(temp)):
                if(temp[k] == i):
                    indegree[i]+=1
    queue = []
    for i in range(1, N+1):
        if(indegree[i] == 0):
            queue.append(i)
    while(queue):
        node = queue.pop(0)
        answer.append(node)
        for nextnode in adj_list[node]:
            idx = nextnode
            indegree[idx] -= 1
            if(indegree[idx] == 0):
                queue.append(idx)

    return answer

if __name__ == "__main__":
    N, M = map(int, input().split())
    for i in range(N):
        init(i+1)
    for i in range(M):
        new_list = list(map(int, input().split()))
        singer_num = new_list[0]
        new_list = new_list[1:]
        for j in range(singer_num-1):
            for k in range(j+1, singer_num):
                if(new_list[k] not in adj_list[new_list[j]]):
                    adj_list[new_list[j]].append(new_list[k])

    answer = topological_sort()

    if(len(answer) != N):
        print(0)
    else:
        for i in answer:
            print(i)