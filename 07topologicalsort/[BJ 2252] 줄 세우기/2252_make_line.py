# 3 2
# 1 3
# 2 3

N, M = map(int, input().split())
in_degree = [0]*(N+1)
arr = {}

if __name__ == "__main__" :
    for i in range(N):
        arr[i+1] = []
    for i in range(M):
        A, B = map(int, input().split())
        arr[A].append(B)
        in_degree[B]+=1
    queue = []
    for i in range(1,N+1):
        if(in_degree[i] == 0):
            queue.append(i)
    answer = []
    while(queue):
        num = queue.pop(0)
        answer.append(num)

        check_list = arr[num]
        for i in check_list:
            in_degree[i]-=1
            if(in_degree[i] == 0):
                queue.append(i)

    for i in answer:
        print(i, end = ' ')