def init(n):
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    return graph

def topological_sort(order_info,n, time):
    answer = [0]*(n+1)
    in_degree = [0]*(n+1)
    #in_degree 계산 
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in order_info[j]:
                if(i == k):
                    in_degree[k]+=1
    queue = []
    for i in range(1, n+1):
        if(in_degree[i] == 0):
            queue.append([i, 0]) #index, starttime
    
    while(queue):
        index, starttime = queue.pop(0)
        for nextnode in order_info[index]:
            answer[nextnode] = max(answer[nextnode], starttime+time[index])
            in_degree[nextnode]-=1
            if(in_degree[nextnode] == 0):
                queue.append([nextnode, answer[nextnode]])

    return answer

if __name__ == "__main__":
    TC = int(input())
    for tc in range(TC):
        N, K = map(int, input().split())
        graph = init(N)
        build_time = list(map(int, input().split()))
        build_time.insert(0, 0)#index 맞춰주기 
        for i in range(K):
            X, Y = map(int, input().split())
            graph[X].append(Y)
        Target_building = int(input())

        answer = topological_sort(graph, N, build_time)
        print(answer[Target_building]+build_time[Target_building])



